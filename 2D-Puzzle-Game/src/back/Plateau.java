package back;

import static java.lang.Math.abs;

public abstract class Plateau {
    protected CasePlateau[][] cases;
    public static final int LARG_CASE = 48;
    public static final int NB_CASES_HAUT = 12;
    public static final int NB_CASES_LARG = 16;
    public static int largeur = NB_CASES_LARG;
    public static int hauteur = NB_CASES_HAUT;
    protected Personnage joueur;

    public Plateau() {
        this.cases = initialiserPlateau();
    }
    
    // Méthode abstraite que chaque sous-classe devra implémenter
    protected abstract CasePlateau[][] initialiserPlateau();
    
    // La méthode initialiserPlateauVide devient une méthode concrète utilisable par les sous-classes
    protected CasePlateau[][] initialiserPlateauVide() {
        CasePlateau[][] plateau = new CasePlateau[hauteur][largeur];
        
        for (int y = 0; y < hauteur; y++) {
            for (int x = 0; x < largeur; x++) {
                // Créer des murs autour du plateau
                if (x == 0 || x == NB_CASES_LARG - 1 || y == 0 || y == NB_CASES_HAUT - 1) {
                    plateau[y][x] = new CasePlateau(CasePlateau.TypeCase.MUR, x, y);
                } else {
                    plateau[y][x] = new CasePlateau(CasePlateau.TypeCase.VIDE, x, y);
                }
            }
        }
        return plateau;
    }

    public CasePlateau[][] getCasesMatrice() {
        return cases;
    }

    public CasePlateau getCase(int vPositionX, int vPositionY) {
        int numCaseX = abs(vPositionX / LARG_CASE);
        int numCaseY = abs(vPositionY / LARG_CASE);
        return cases[numCaseY][numCaseX];
    }


    public boolean estCaseVide(int vPositionX, int vPositionY) {
        CasePlateau casePlateau = getCase(vPositionX, vPositionY);
        return casePlateau != null && casePlateau.getType() == CasePlateau.TypeCase.VIDE;
    }

    public int getLargeur() {
        return largeur;
    }

    public int getHauteur() {
        return hauteur;
    }


    public void reinitialiserPlateau() {
        cases = initialiserPlateau();
    }
    
    public abstract Plateau plateauPlein();
}