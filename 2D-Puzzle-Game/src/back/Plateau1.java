package back;


public class Plateau1 extends Plateau {

    @Override
    protected CasePlateau[][] initialiserPlateau() {
        CasePlateau[][] plateau = initialiserPlateauVide();


        //des murs
            for (int y = 0; y <= 5; y++) {
            plateau[3][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
            for (int y = 9; y <= 11; y++) {
            plateau[3][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
            for (int y = 4; y <= 14; y++) {
            plateau[5][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
             for (int y = 0; y <= 11; y++) {
            plateau[7][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
            for (int y = 3; y <= 14; y++) {
            plateau[9][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
               // obstacles 
        plateau[0][0] = new CasePlateau(CasePlateau.TypeCase.COEUR, 0, 0);
        plateau[0][1] = new CasePlateau(CasePlateau.TypeCase.VIE, 0, 1);
        plateau[4][7] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 4, 3);
        plateau[8][13] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 4, 3);
        plateau[8][14] = new CasePlateau(CasePlateau.TypeCase.CLEF, 4, 3);
        plateau[6][1] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 6, 4);
        plateau[6][2] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 6, 4);
        plateau[6][10] = new CasePlateau(CasePlateau.TypeCase.POMME, 4, 3);
        plateau[10][1] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 6, 4);
            
           


        
        // Placement de la porte (sortie vers le plateau 2)
        int porteX = NB_CASES_LARG - 2;
        int porteY = NB_CASES_HAUT - 2;
        plateau[porteY][porteX] = new CasePlateau(CasePlateau.TypeCase.PORTE_FERMEE, porteX, porteY);

        return plateau;
    }

    @Override
    public Plateau plateauPlein() {
        return this;
    }
}
