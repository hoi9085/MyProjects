package back;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class PersonnageTest {

    private Personnage perso;
    private Plateau plateau;

    @BeforeEach
    public void setup() {
        perso = new Personnage("Héros", 3, 1, 1);
        plateau = new Plateau() {
            {
                this.setCasesMatrice(initialiserPlateauVide());
                getCasesMatrice()[2][1] = new CasePlateau(CasePlateau.TypeCase.LAVE, 1, 2); // Dangereux
                getCasesMatrice()[1][2] = new CasePlateau(CasePlateau.TypeCase.MUR, 2, 1); // Obstruant
            }
        };
    }

    @Test
    public void testConstructeurEtGetters() {
        assertEquals("Héros", perso.getNom());
        assertEquals(1, perso.getPositionX());
        assertEquals(1, perso.getPositionY());
        assertEquals(3, perso.getVie());
    }

    @Test
    public void testSetters() {
        perso.setPositionX(4);
        perso.setPositionY(5);
        perso.setVie(2);
        perso.setNom("Autre");

        assertEquals(4, perso.getPositionX());
        assertEquals(5, perso.getPositionY());
        assertEquals(2, perso.getVie());
        assertEquals("Autre", perso.getNom());
    }

    @Test
    public void testSubirDegatsEtEstMort() {
        perso.subirDegats(1);
        assertEquals(2, perso.getVie());
        perso.subirDegats(5);
        assertEquals(0, perso.getVie());
        assertTrue(perso.estMort());
    }

    @Test
    public void testGagnerVie() {
        perso.setVie(2);
        perso.gagnerVie();
        assertEquals(3, perso.getVie());
        perso.gagnerVie(); // pas au-delà
        assertEquals(3, perso.getVie());
    }

    @Test
    public void testSeDeplacerValide() {
        boolean result = perso.seDeplacer(0, 1, plateau); // en bas, vers lave
        assertTrue(result);
        assertEquals(1, perso.getPositionX());
        assertEquals(2, perso.getPositionY());
        assertEquals(2, perso.getVie()); // Subit un dégât
    }

    @Test
    public void testSeDeplacerMur() {
        boolean result = perso.seDeplacer(1, 0, plateau); // droite = mur
        assertFalse(result);
        assertEquals(1, perso.getPositionX());
        assertEquals(1, perso.getPositionY());
    }

    @Test
    public void testReinitialiserPosition() {
        perso.reinitialiserPosition();
        assertEquals(0, perso.getPositionX());
        assertEquals(0, perso.getPositionY());
    }

    @Test
    public void testGravite() {
        assertTrue(perso.estAffecteeParGravite());
        perso.setAffecteeParGravite(false);
        assertFalse(perso.estAffecteeParGravite());

        perso.setVitesseX(2.5f);
        perso.setVitesseY(3.5f);
        assertEquals(2.5f, perso.getVitesseX());
        assertEquals(3.5f, perso.getVitesseY());
    }

    @Test
    public void testClePossedee() {
        assertFalse(perso.aCle());
        perso.setClePossedee(true);
        assertTrue(perso.aCle());
    }

    @Test
    public void testEtatAuSol() {
        assertTrue(perso.estAuSol());
        perso.setEstAuSol(false);
        assertFalse(perso.estAuSol());
    }

    @Test
    public void testTouches() {
        perso.setToucheDroitePressee(true);
        perso.setToucheGauchePressee(true);
        perso.setToucheSautPressee(true);

        assertTrue(perso.isToucheDroitePressee());
        assertTrue(perso.isToucheGauchePressee());
        assertTrue(perso.isToucheSautPressee());
    }

    @Test
    public void testAfficherPerso() {
        String expected = "Personnage{nom='Héros', vie=3}";
        assertEquals(expected, perso.afficherPerso());
    }
}
