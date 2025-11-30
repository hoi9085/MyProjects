package back;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class GestionnaireNiveauxTest {

    @Test
    public void testChargerNiveau1() {
        GestionnaireNiveaux gestionnaire = new GestionnaireNiveaux();
        Plateau niveau = gestionnaire.chargerNiveau(1);

        assertNotNull(niveau);
        assertTrue(niveau instanceof Plateau1);
        assertEquals(niveau, gestionnaire.getPlateauActuel());
    }

    @Test
    public void testChargerNiveau2() {
        GestionnaireNiveaux gestionnaire = new GestionnaireNiveaux();
        Plateau niveau = gestionnaire.chargerNiveau(2);

        assertNotNull(niveau);
        assertTrue(niveau instanceof Plateau2);
        assertEquals(niveau, gestionnaire.getPlateauActuel());
    }

    @Test
    public void testChargerNiveau3() {
        GestionnaireNiveaux gestionnaire = new GestionnaireNiveaux();
        Plateau niveau = gestionnaire.chargerNiveau(3);

        assertNotNull(niveau);
        assertTrue(niveau instanceof Plateau3);
        assertEquals(niveau, gestionnaire.getPlateauActuel());
    }

    @Test
    public void testChargerNiveauInexistant() {
        GestionnaireNiveaux gestionnaire = new GestionnaireNiveaux();
        Plateau niveau = gestionnaire.chargerNiveau(999);

        assertNull(niveau);
        assertNull(gestionnaire.getPlateauActuel());
    }
}
