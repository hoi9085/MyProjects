package back;

public class Personnage implements EntitePhysique {
    // Attributs
    private String nom;
    private int positionX;
    private int positionY;
    private float vitesseX = 0;
    private float vitesseY = 0;
    private int vie;
    private int vitesse;
    private boolean estAuSol = true;
    private boolean affecteParGravite = true;
 // Variables de contrôle des touches
    private boolean toucheDroitePressee = false;
    private boolean toucheGauchePressee = false;
    private boolean toucheSautPressee = false;
    private boolean clePossedee;
	private boolean enContactAvecDanger;
    

    // Constructeurs
    public Personnage(String nom, int positionX, int positionY) {
        this.nom = nom;
        this.vie = 3; // Nbr de vies par défaut
        this.positionX = positionX; // Position par défaut
        this.positionY = positionY; // Position par défaut
        this.vitesse = 1; // Vitesse par défaut
    }

    public Personnage(String nom, int vie, int positionX, int positionY) {
        this.nom = nom;
        this.vie = vie;
        this.positionX = positionX; // Position par défaut
        this.positionY = positionY; // Position par défaut
        this.vitesse = 1; // Vitesse par défaut
    }

    private boolean caseObstruante(int futurX, int futurY, Plateau plateau) {
        CasePlateau coinHautGauche = plateau.getCase(futurX, futurY);
        CasePlateau coinHautDroit = plateau.getCase(futurX + Plateau.LARG_CASE - 1, futurY);
        CasePlateau coinBasGauche = plateau.getCase(futurX, futurY + Plateau.LARG_CASE - 1);
        CasePlateau coinBasDroit = plateau.getCase(futurX + Plateau.LARG_CASE - 1, futurY + Plateau.LARG_CASE - 1);
        return coinHautGauche.estObstruant() || coinHautDroit.estObstruant() ||
                coinBasGauche.estObstruant() || coinBasDroit.estObstruant();
    }

    // déplacer le personnage
    public boolean seDeplacer(int deltaX, int deltaY, Plateau plateau) {
        int futurX = this.positionX + deltaX;
        int futurY = this.positionY + deltaY;
        
        // Vérifier si le déplacement est possible
        if (!caseObstruante(futurX, futurY, plateau)) {
            this.positionX = futurX;
            this.positionY = futurY;
            
            // Si on se déplace vers le bas, on n'est plus au sol (on tombe)
            if (deltaY > 0) {
                this.estAuSol = false;
            }
            
            return true; // Déplacement réussi
        }
        int centreX = futurX + Plateau.LARG_CASE / 2;
        int centreY = futurY + Plateau.LARG_CASE / 2;
        CasePlateau caseCentre = plateau.getCase(centreX, centreY);

        if (caseCentre != null && caseCentre.estDanger()) {
            if (!this.enContactAvecDanger) {
                this.subirDegats(1); // on ne subit qu'une fois
                this.enContactAvecDanger = true;
            }
        } else {
            // On a quitté la zone dangereuse
            this.enContactAvecDanger = false;
        }

        // Si on ne peut pas se déplacer vers le bas, on est au sol
        if (deltaY > 0) {
            this.estAuSol = true;
        }
        
        return false; // Déplacement impossible
    }

    public void setClePossedee(boolean b) {
        this.clePossedee = b;
    }

    public boolean aCle() {
        return clePossedee;
    }

    // subir des dégâts
    public void subirDegats(int degats) {
        this.vie -= degats;
        if (this.vie < 0) {
            this.vie = 0; // La vie ne peut pas être négative
        }
    }

    public void gagnerVie() {
        if (vie < 3) {
            vie++;
        }
    }

    // vérifier si le personnage est mort
    public boolean estMort() {
        return this.vie == 0;
    }

    // réinitialiser la position du personnage
    public void reinitialiserPosition() {
        this.positionX = 0;
        this.positionY = 0;
    }

    // Getters et Setters
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public int getPositionX() {
        return positionX;
    }

    public void setPositionX(int positionX) {
        this.positionX = positionX;
    }

    public int getPositionY() {
        return positionY;
    }

    public void setPositionY(int positionY) {
        this.positionY = positionY;
    }

    public int getVie() {
        return vie;
    }

    public void setVie(int vie) {
        this.vie = vie;
    }

    public int getVitesse() {
        return vitesse;
    }

    public void setVitesse(int vitesse) {
        this.vitesse = vitesse;
    }

    // Implémentation de l'interface EntitePhysique
    @Override
    public float getVitesseX() {
        return vitesseX;
    }

    @Override
    public float getVitesseY() {
        return vitesseY;
    }

    @Override
    public void setVitesseX(float vx) {
        this.vitesseX = vx;
    }

    @Override
    public void setVitesseY(float vy) {
        this.vitesseY = vy; 
    }

    @Override
    public boolean estAffecteeParGravite() {
        return affecteParGravite;
    }

    @Override
    public void setAffecteeParGravite(boolean affecte) {
        this.affecteParGravite = affecte;
    }

    /**
     * Indique si le personnage est au sol.
     * 
     * @return true si le personnage est au sol, false sinon
     */
    public boolean estAuSol() {
        return estAuSol;
    }
    
    /**
     * Définit si le personnage est au sol.
     * 
     * @param estAuSol true si le personnage est au sol, false sinon
     */
    public void setEstAuSol(boolean estAuSol) {
        this.estAuSol = estAuSol;
    }

    // afficher le nom du personnage et sa vie
    public String afficherPerso() {
        return "Personnage{" +
                "nom='" + nom + '\'' + ", vie=" + vie + '}';
    }

	public boolean isToucheDroitePressee() {
		return toucheDroitePressee;
	}

	public void setToucheDroitePressee(boolean toucheDroitePressee) {
		this.toucheDroitePressee = toucheDroitePressee;
	}

	public boolean isToucheGauchePressee() {
		return toucheGauchePressee;
	}

	public void setToucheGauchePressee(boolean toucheGauchePressee) {
		this.toucheGauchePressee = toucheGauchePressee;
	}

	public boolean isToucheSautPressee() {
		return toucheSautPressee;
	}

	public void setToucheSautPressee(boolean toucheSautPressee) {
		this.toucheSautPressee = toucheSautPressee;
	}
}
