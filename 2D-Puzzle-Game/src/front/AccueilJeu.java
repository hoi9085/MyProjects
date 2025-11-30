package front;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AccueilJeu extends JFrame {

    public AccueilJeu() {
        setTitle("Accueil");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setResizable(false);

        // Fond d'écran personnalisé
        JPanel fenetre = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                ImageIcon fond = new ImageIcon(getClass().getResource("/front/images/main.png"));
                g.drawImage(fond.getImage(), 0, 0, getWidth(), getHeight(), this);
            }
        };
        fenetre.setLayout(null); // Positionnement libre

        // Bouton Start
        JButton boutonCommencer = new JButton("START");
        boutonCommencer.setBounds(300, 350, 200, 50);
        boutonCommencer.setFont(new Font("Book Antiqua", Font.BOLD, 24));
        boutonCommencer.setForeground(Color.WHITE); // texte blanc
        boutonCommencer.setBackground(new Color(80, 0, 0)); // fond rouge foncé
        boutonCommencer.setBorder(BorderFactory.createLineBorder(Color.LIGHT_GRAY, 3));
        boutonCommencer.setFocusPainted(false);
        boutonCommencer.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Démarrer le jeu
                dispose(); // Fermer la page d’accueil
                LancementJeu.demarrerJeu();
            }
        });

        // Bouton Exit
        JButton boutonQuitter = new JButton("EXIT");
        boutonQuitter.setBounds(300, 420, 200, 50);
        boutonQuitter.setFont(new Font("Book Antiqua", Font.BOLD, 24));
        boutonQuitter.setForeground(Color.WHITE); // texte blanc
        boutonQuitter.setBackground(new Color(80, 0, 0)); // fond rouge foncé
        boutonQuitter.setBorder(BorderFactory.createLineBorder(Color.LIGHT_GRAY, 3));
        boutonQuitter.setFocusPainted(false);
        boutonQuitter.addActionListener(e -> System.exit(0));

        // Ajout des composants
        fenetre.add(boutonCommencer);
        fenetre.add(boutonQuitter);
        setContentPane(fenetre);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            AccueilJeu accueil = new AccueilJeu();
            accueil.setVisible(true);
        });
    }
}

