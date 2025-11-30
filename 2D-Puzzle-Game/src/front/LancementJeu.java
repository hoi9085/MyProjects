package front;
import javax.swing.*;
import back.*;

public class LancementJeu {

    public static void demarrerJeu() {
        JFrame fenetre = new JFrame("Jeu Projet Long");
        fenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Scene scene = new Scene();
        fenetre.setContentPane(scene);

        fenetre.setSize(Plateau.NB_CASES_LARG * Plateau.LARG_CASE, Plateau.NB_CASES_HAUT * Plateau.LARG_CASE);
        fenetre.setLocationRelativeTo(null);
        fenetre.setResizable(false);
        fenetre.setVisible(true);

        scene.setUpGame();
    }
}

