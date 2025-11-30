package back;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class SystemePhysiqueTest {

    private SystemePhysique systemePhysique;
    private EntitePhysique entite;

    @BeforeEach
    public void setUp() {
        // Exemple : gravité 9.8 m/s², vitesse max 50
        systemePhysique = new SystemePhysique(9.8f, 50f);
        // Création d'une entité fictive avec vitesse initiale nulle
        entite = new EntitePhysique();
        entite.setVitesseY(0f);
        entite.setPositionY(100f); // position initiale en hauteur
    }

    @Test
    public void testGraviteAppliquee() {
        float deltaTemps = 1f; // 1 seconde écoulée

        // Appliquer la gravité
        systemePhysique.mettreAJour(entite, deltaTemps);

        // La vitesse Y devrait avoir augmenté à cause de la gravité
        assertTrue(entite.getVitesseY() > 0, "La vitesse verticale doit augmenter sous gravité");

        // La position Y devrait avoir diminué (l'entité descend)
        assertTrue(entite.getPositionY() < 100f, "La position verticale doit diminuer sous gravité");

        // Vérifier que la vitesse ne dépasse pas la vitesse max
        assertTrue(entite.getVitesseY() <= 50f, "La vitesse verticale ne doit pas dépasser la vitesse maximale");
    }
}
