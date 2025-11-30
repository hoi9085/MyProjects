package front;

import back.CasePlateau;
import back.GestionnairePlateaux;
import back.Personnage;
import back.Plateau;
import back.SystemePhysique;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.RenderingHints;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.HashMap;
import java.util.Map;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import javax.swing.Timer;

public class Scene extends JPanel implements ActionListener {
    
    private Plateau plateau;
    private Map<CasePlateau.TypeCase, Image> tileImages;

    private Personnage perso1, perso2;
    private Graphics2D g;
    
    // Timer pour la boucle de jeu
    private Timer gameTimer;
    private final int DELAY = 17; // ~60 FPS
    private final float DELTA_TEMPS = 0.017f; // En secondes (17ms)
    
    // Système physique
    private SystemePhysique systemePhysique;
    private final float INTENSITE_GRAVITE = 980.0f; // pixels par seconde²
    private final float VITESSE_MAX_CHUTE = 500.0f; // pixels par seconde
    private final float FORCE_SAUT = -400.0f; // Force négative car vers le haut

    // Constantes de mouvement
    private final float VITESSE_HORIZONTALE = 200.0f; // pixels par seconde

    private GestionnairePlateaux gestionnaireNiveaux;
    private int numeroNiveauActuel = 1;

    
    Sound sound = new Sound();

    public Scene() {
        super();

        this.gestionnaireNiveaux = new GestionnairePlateaux();
        this.plateau = gestionnaireNiveaux.chargerNiveau(numeroNiveauActuel);
        this.perso1 = new Personnage("Chevalier", 100, 80);
        this.perso2 = new Personnage("Chevalier2", 50, 80);
        

        // Initialiser le système physique
        this.systemePhysique = new SystemePhysique(INTENSITE_GRAVITE, VITESSE_MAX_CHUTE);
        
        loadTileImages();

        setFocusable(true);
        requestFocusInWindow();
        
        // Initialiser le timer
        gameTimer = new Timer(DELAY, this);
        gameTimer.start();
        
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                int key = e.getKeyCode();

                if (key == KeyEvent.VK_D) {
                    perso1.setToucheDroitePressee(true);
                }
                if (key == KeyEvent.VK_Q) {
                    perso1.setToucheGauchePressee(true);
                }
                
                // Pour le saut, on enregistre la touche
                if (key == KeyEvent.VK_SPACE) {
                    perso1.setToucheSautPressee(true);
                }
                if (key == KeyEvent.VK_RIGHT) {
                	perso2.setToucheDroitePressee(true);
                }
                if (key == KeyEvent.VK_LEFT) {
                	perso2.setToucheGauchePressee(true);
                }
                if (key == KeyEvent.VK_UP) {
                	perso2.setToucheSautPressee(true);
                }
                if (key == KeyEvent.VK_ENTER) {
                    int x = perso1.getPositionX() + Plateau.LARG_CASE / 2;
                    int y = perso1.getPositionY() + Plateau.LARG_CASE / 2;
                    CasePlateau caseActuelle1 = plateau.getCase(x, y);

                    int x2 = perso2.getPositionX() + Plateau.LARG_CASE / 2;
                    int y2 = perso2.getPositionY() + Plateau.LARG_CASE / 2;
                    CasePlateau caseActuelle2 = plateau.getCase(x2, y2);

                    if (caseActuelle1.getType() == CasePlateau.TypeCase.ETOILE || caseActuelle2.getType() == CasePlateau.TypeCase.ETOILE) {
                        afficherEcranFin();
                    }
                    
                	interagir(perso2);
                    interagir(perso1);
                }
            }
            
            @Override
            public void keyReleased(KeyEvent e) {
                int key = e.getKeyCode();
                
                if (key == KeyEvent.VK_D) {
                    perso1.setToucheDroitePressee(false);
                }
                if (key == KeyEvent.VK_Q) {
                    perso1.setToucheGauchePressee(false);
                }
                
                if (key == KeyEvent.VK_SPACE) {
                    perso1.setToucheSautPressee(false);
                }
                if (key == KeyEvent.VK_RIGHT) {
                	perso2.setToucheDroitePressee(false);
                }
                if (key == KeyEvent.VK_LEFT) {
                	perso2.setToucheGauchePressee(false);
                }
                if (key == KeyEvent.VK_UP) {
                	perso2.setToucheSautPressee(false);
                }
            }
        });
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // Cette méthode est appelée par le timer à intervalle régulier
        gererEntrees(perso1);
        gererEntrees(perso2);
        mettreAJourPhysique(perso1);
        mettreAJourPhysique(perso2);
        repaint();
        if (perso1.estMort() || perso2.estMort()) {
        	afficherEcranFin();
        }
    }

    private void interagir(Personnage p) {
        int x = p.getPositionX() + Plateau.LARG_CASE / 2;
        int y = p.getPositionY() + Plateau.LARG_CASE / 2;

        // Récupérer la case actuelle (ou devant selon direction)
        CasePlateau caseActuelle = plateau.getCase(x, y);
        
        if (caseActuelle != null) {
            CasePlateau.TypeCase type = caseActuelle.getType();
            
            switch (type) {
                case CLEF:
                    // Ramasser la clé
                    p.setClePossedee(true); 
                    caseActuelle.setType(CasePlateau.TypeCase.VIDE);
                    break;

                
                case PORTE_FERMEE:
                    if (p.aCle()) {
                        caseActuelle.setType(CasePlateau.TypeCase.PORTE_OUVERTE);
                        changerDeNiveau();
                    }
                    break;

                case POMME:
                    p.gagnerVie(); // augmente la vie
                    caseActuelle.setType(CasePlateau.TypeCase.VIDE);
                    break;
                default:
                    break;
            }
        }
    }

    
    private void gererEntrees(Personnage p) {
        // Gérer le mouvement horizontal en fonction des touches pressées
        if (p.isToucheDroitePressee() && !p.isToucheGauchePressee()) {
            p.setVitesseX(VITESSE_HORIZONTALE);
        } else if (p.isToucheGauchePressee() && !p.isToucheDroitePressee()) {
            p.setVitesseX(-VITESSE_HORIZONTALE);
        } else {
            // Arrêter le mouvement horizontal si aucune touche n'est pressée
            p.setVitesseX(0);
        }
        
        // Gérer le saut
        if (p.isToucheSautPressee() && p.estAuSol()) {
            p.setVitesseY(FORCE_SAUT);
            p.setEstAuSol(false);
            try {
                playSoundEffect(1); // Son de saut (si disponible)
            } catch (Exception ex) {
                // Ignorer silencieusement l'erreur si le son échoue
            }
        }
    }
    
    private void mettreAJourPhysique(Personnage perso) {
        // Appliquer la gravité au personnage
        systemePhysique.mettreAJour(perso, DELTA_TEMPS);
        
        // Calculer le déplacement basé sur les vitesses (en pixels)
        float deplacementX = perso.getVitesseX() * DELTA_TEMPS;
        float deplacementY = perso.getVitesseY() * DELTA_TEMPS;
        
        // Appliquer le déplacement horizontal
        if (deplacementX != 0) {
            int deplX = Math.round(deplacementX);
            perso.seDeplacer(deplX, 0, plateau);
        }
        
        // Appliquer le déplacement vertical
        if (deplacementY != 0) {
            int deplY = Math.round(deplacementY);
            boolean aBouge = perso.seDeplacer(0, deplY, plateau);
            
            // Si le personnage n'a pas pu se déplacer verticalement, c'est qu'il y a collision
            if (!aBouge) {
                // Si le personnage allait vers le bas (vitesse positive), il est maintenant au sol
                if (perso.getVitesseY() > 0) {
                    perso.setEstAuSol(true);
                }
                // Dans tous les cas, arrêter le mouvement vertical
                perso.setVitesseY(0);
            }
        }
        
        // Vérifier si le personnage est sur le sol
        verifierSol(perso);
    }
    
    private void verifierSol(Personnage perso) {
        // On vérifie si le personnage est déjà au sol
        if (perso.estAuSol()) {
            return;
        }
        
        // Vérifier s'il y a un bloc solide juste en-dessous du personnage
        int posX = perso.getPositionX();
        int posY = perso.getPositionY() + Plateau.LARG_CASE;
        
        // Vérifier les coins bas du personnage
        int coinBasGaucheX = posX;
        int coinBasDroitX = posX + Plateau.LARG_CASE - 1;
        
        // Obtenir les cases sous les pieds
        CasePlateau caseGauche = plateau.getCase(coinBasGaucheX, posY);
        CasePlateau caseDroite = plateau.getCase(coinBasDroitX, posY);
        
        // Si l'une des cases est obstruante, le personnage est au sol
        if ((caseGauche != null && caseGauche.estObstruant()) || 
            (caseDroite != null && caseDroite.estObstruant())) {
            perso.setEstAuSol(true);
            perso.setVitesseY(0);
        } else {
            // Le personnage n'est pas au sol s'il n'y a pas de bloc solide en-dessous
            // et qu'il n'est pas déjà en train de sauter
            if (perso.getVitesseY() == 0) {
                perso.setEstAuSol(false);
            }
        }
    }

    private void changerDeNiveau() {
        numeroNiveauActuel++;
        Plateau nouveauNiveau = gestionnaireNiveaux.chargerNiveau(numeroNiveauActuel);
        
        if (nouveauNiveau != null) {
            this.plateau = nouveauNiveau;
            // Réinitialiser les personnages 
            perso1.setPositionX(100);
            perso1.setPositionY(80);
            perso2.setPositionX(50);
            perso2.setPositionY(80);
            perso1.setClePossedee(false);
            perso2.setClePossedee(false);
            perso1.setEstAuSol(false);
            perso2.setEstAuSol(false);
        } else {
            // Niveau non trouvé 
            stopMusic();
            System.out.println("Fin du jeu");
            gameTimer.stop();
        }
    }

    private void afficherEcranFin() {
        gameTimer.stop(); // arrête le jeu

        JFrame fenetreFin = new JFrame("Fin du jeu");
        fenetreFin.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fenetreFin.setSize(400, 200);
        fenetreFin.setLocationRelativeTo(null);

        JPanel panel = new JPanel();
        panel.setBackground(Color.BLACK);

        JLabel label = new JLabel("Fin du Jeu");
        label.setForeground(Color.WHITE);
        label.setFont(new Font("Arial", Font.BOLD, 18));
        label.setHorizontalAlignment(SwingConstants.CENTER);

        panel.add(label);
        fenetreFin.add(panel);

        fenetreFin.setVisible(true);
    }


    private void loadTileImages() {
        tileImages = new HashMap<>();
    
        tileImages.put(CasePlateau.TypeCase.MUR, new ImageIcon(getClass().getResource("/front/res/tiles/test_sol.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.VIDE, new ImageIcon(getClass().getResource("/front/res/tiles/test_brick.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.JOUEUR1, new ImageIcon(getClass().getResource("/front/res/tiles/chevalier.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.JOUEUR2, new ImageIcon(getClass().getResource("/front/res/tiles/chevalier2.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.BARRIL, new ImageIcon(getClass().getResource("/front/res/tiles/barril.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.CIBLE, new ImageIcon(getClass().getResource("/front/res/tiles/cible_paille.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.CLEF, new ImageIcon(getClass().getResource("/front/res/tiles/clef.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.LAVE, new ImageIcon(getClass().getResource("/front/res/tiles/lave.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.PIQUE, new ImageIcon(getClass().getResource("/front/res/tiles/pique.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.POMME, new ImageIcon(getClass().getResource("/front/res/tiles/pomme.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.PORTE_FERMEE, new ImageIcon(getClass().getResource("/front/res/tiles/porte_fermee.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.PORTE_OUVERTE, new ImageIcon(getClass().getResource("/front/res/tiles/porte_ouverte.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.COEUR, new ImageIcon(getClass().getResource("/front/res/tiles/coeur.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.VIE, new ImageIcon(getClass().getResource("/front/res/tiles/vie3.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.VIE0, new ImageIcon(getClass().getResource("/front/res/tiles/vie0.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.VIE1, new ImageIcon(getClass().getResource("/front/res/tiles/vie1.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.VIE2, new ImageIcon(getClass().getResource("/front/res/tiles/vie2.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.VIE3, new ImageIcon(getClass().getResource("/front/res/tiles/vie3.png")).getImage());
        tileImages.put(CasePlateau.TypeCase.ETOILE, new ImageIcon(getClass().getResource("/front/res/tiles/etoile_mur.png")).getImage());
    }

    /** Initialise le jeu lors de son lancement. */
    public void setUpGame() {
        this.playMainMusic(0);
    }

    /** Joue la musique principale du jeu.
     * Cette musique peut varier suivant le donjon, salle commune ou
     * salle du boss, menu du jeu, etc.
     * @param i index de l'URL du son
     */
    public void playMainMusic(int i) {
        sound.setFile(i);
        sound.play();
        sound.loop();
    }

    /** Coupe la musique en cours. */
    public void stopMusic() {
        sound.stop();
    }

    /** Joue un effet sonore au milieu de la partie,
     * comme un bruit de pas ou une porte qui s'ouvre.
     * @param i index de l'URL du son
     */
    public void playSoundEffect(int i) {
        sound.setFile(i);
        sound.play();
    }

    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        this.g = (Graphics2D)g;

        // antialiasing, pour rendre les contours plus lisses
        this.g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        CasePlateau[][] cases = plateau.getCasesMatrice();
        dessiner(cases);
        this.g.drawImage(tileImages.get(CasePlateau.TypeCase.JOUEUR1), perso1.getPositionX(), perso1.getPositionY(), Plateau.LARG_CASE, Plateau.LARG_CASE, this);
        this.g.drawImage(tileImages.get(CasePlateau.TypeCase.JOUEUR2), perso2.getPositionX(), perso2.getPositionY(), Plateau.LARG_CASE, Plateau.LARG_CASE, this);

    }

    public void dessiner(CasePlateau[][] cases){
        Image imgvide = tileImages.get(CasePlateau.TypeCase.VIDE);
        Image imgmur = tileImages.get(CasePlateau.TypeCase.MUR);
        for (int y = 0; y < plateau.getHauteur(); y++) {
            for (int x = 0; x < plateau.getLargeur(); x++) {
                CasePlateau.TypeCase type = cases[y][x].getType(); // pas y x
                Image img = tileImages.get(type);

                if (img != null) {
                        switch (type) {
                            case LAVE:
                                this.g.drawImage(imgvide, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                                break;
                            case PIQUE:
                                this.g.drawImage(imgvide, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                                break;
                            case POMME:
                                this.g.drawImage(imgvide, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                                break;
                            case PORTE_OUVERTE:
                                this.g.drawImage(imgvide, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                                break;
                            case PORTE_FERMEE:
                                this.g.drawImage(imgvide, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                                break;
                            case CLEF:
                                this.g.drawImage(imgvide, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                                break;
                            case CIBLE:
                                this.g.drawImage(imgvide, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                                break;
                            case BARRIL:
                                this.g.drawImage(imgvide, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                                break;
                            case COEUR:
                                this.g.drawImage(imgmur, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                                break;
                            case VIE:
                                this.g.drawImage(imgmur, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                                int i = perso1.getVie();
                                if (perso2.getVie() < i) {
                                    i = perso2.getVie();
                                } switch (i) {
                                    case 0:
                                        img = tileImages.get(CasePlateau.TypeCase.VIE0);
                                        break;
                                    case 1:
                                        img = tileImages.get(CasePlateau.TypeCase.VIE1);
                                        break;
                                    case 2:
                                        img = tileImages.get(CasePlateau.TypeCase.VIE2);
                                        break;
                                    case 3:
                                        img = tileImages.get(CasePlateau.TypeCase.VIE3);
                                        break;
                                    default:
                                }
                                break;
                            default:
                                break;
                        }
                        this.g.drawImage(img, x * Plateau.LARG_CASE, y * Plateau.LARG_CASE, Plateau.LARG_CASE, Plateau.LARG_CASE, this);
                }
            }
        }
    }
}
