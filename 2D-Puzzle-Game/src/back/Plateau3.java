package back;


public class Plateau3 extends Plateau {

    @Override
    protected CasePlateau[][] initialiserPlateau() {
        CasePlateau[][] plateau = initialiserPlateauVide();


        //des murs
            for (int y = 0; y <= 3; y++) {
            plateau[3][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
            for (int y = 6; y <= 7; y++) {
            plateau[3][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
            for (int y = 10; y <= 14; y++) {
            plateau[3][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
            for (int y = 6; y <= 7; y++) {
            plateau[5][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
            for (int y = 13; y <= 14; y++) {
            plateau[5][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
            for (int y = 0; y <= 12; y++) {
            plateau[7][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
            for (int y = 4; y <= 6; y++) {
            plateau[9][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
            for (int y = 10; y <= 14; y++) {
            plateau[9][y] = new CasePlateau(CasePlateau.TypeCase.MUR, y, 5); // mur horizontal central
            }
               // obstacles
        plateau[0][0] = new CasePlateau(CasePlateau.TypeCase.COEUR, 0, 0);
        plateau[0][1] = new CasePlateau(CasePlateau.TypeCase.VIE, 0, 1);
        
        plateau[2][1] = new CasePlateau(CasePlateau.TypeCase.PORTE_OUVERTE, 4, 3);
        plateau[2][14] = new CasePlateau(CasePlateau.TypeCase.CIBLE, 4, 3);
        plateau[2][11] = new CasePlateau(CasePlateau.TypeCase.BARRIL, 4, 3);
        
        plateau[4][6] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 4, 3);
        plateau[4][7] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 4, 3);
        //plateau[4][11] = new CasePlateau(CasePlateau.TypeCase.POMME, 4, 3);
       
        plateau[8][14] = new CasePlateau(CasePlateau.TypeCase.LAVE, 4, 3);
        
        plateau[6][1] = new CasePlateau(CasePlateau.TypeCase.LAVE, 6, 4);
        plateau[6][2] = new CasePlateau(CasePlateau.TypeCase.LAVE, 6, 4);
        plateau[6][3] = new CasePlateau(CasePlateau.TypeCase.POMME, 6, 4);
        plateau[6][4] = new CasePlateau(CasePlateau.TypeCase.LAVE, 6, 4);
        plateau[6][9] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 6, 4);
        plateau[6][11] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 6, 4);

        plateau[10][2] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 6, 4);
        plateau[10][1] = new CasePlateau(CasePlateau.TypeCase.POMME, 6, 4);
        plateau[10][7] = new CasePlateau(CasePlateau.TypeCase.POMME, 6, 4);
        plateau[10][8] = new CasePlateau(CasePlateau.TypeCase.PIQUE, 6, 4);
        
            



        
        // Placement de la porte (sortie vers le plateau 2)
        int porteX = NB_CASES_LARG - 2;
        int porteY = NB_CASES_HAUT - 2;
        plateau[porteY][porteX] = new CasePlateau(CasePlateau.TypeCase.ETOILE, porteX, porteY);

        return plateau;
    }

    @Override
    public Plateau plateauPlein() {
        return this;
    }
}

