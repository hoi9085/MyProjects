package back;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class CasePlateauTest {

    @Test
    public void testInitialisationObstruant() {
        CasePlateau mur = new CasePlateau(CasePlateau.TypeCase.MUR, 0, 0);
        assertTrue(mur.estObstruant());
        assertFalse(mur.estDanger());

        CasePlateau barril = new CasePlateau(CasePlateau.TypeCase.BARRIL, 1, 1);
        assertTrue(barril.estObstruant());

        CasePlateau cible = new CasePlateau(CasePlateau.TypeCase.CIBLE, 2, 2);
        assertTrue(cible.estObstruant());

        CasePlateau vide = new CasePlateau(CasePlateau.TypeCase.VIDE, 3, 3);
        assertFalse(vide.estObstruant());
    }

    @Test
    public void testInitialisationDanger() {
        CasePlateau pique = new CasePlateau(CasePlateau.TypeCase.PIQUE, 0, 0);
        assertTrue(pique.estDanger());

        CasePlateau lave = new CasePlateau(CasePlateau.TypeCase.LAVE, 1, 1);
        assertTrue(lave.estDanger());

        CasePlateau pomme = new CasePlateau(CasePlateau.TypeCase.POMME, 2, 2);
        assertFalse(pomme.estDanger());
    }

    @Test
    public void testGetters() {
        CasePlateau caseTest = new CasePlateau(CasePlateau.TypeCase.POMME, 5, 6);
        assertEquals(CasePlateau.TypeCase.POMME, caseTest.getType());
        assertEquals(5, caseTest.getPositionX());
        assertEquals(6, caseTest.getPositionY());
    }

    @Test
    public void testSetters() {
        CasePlateau caseTest = new CasePlateau(CasePlateau.TypeCase.VIDE, 0, 0);
        caseTest.setType(CasePlateau.TypeCase.CLEF);
        assertEquals(CasePlateau.TypeCase.CLEF, caseTest.getType());

        caseTest.setPositionX(10);
        caseTest.setPositionY(20);
        assertEquals(10, caseTest.getPositionX());
        assertEquals(20, caseTest.getPositionY());

        caseTest.setObstruant(true);
        caseTest.setDanger(true);
        assertTrue(caseTest.estObstruant());
        assertTrue(caseTest.estDanger());
    }
}
