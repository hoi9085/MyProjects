package back;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class GraviteTest {

    private static class FakeEntite implements EntitePhysique {
        private float vx = 0f;
        private float vy = 0f;
        private boolean gravite = true;

        @Override public float getVitesseX() { return vx; }
        @Override public float getVitesseY() { return vy; }
        @Override public void setVitesseX(float vx) { this.vx = vx; }
        @Override public void setVitesseY(float vy) { this.vy = vy; }
        @Override public boolean estAffecteeParGravite() { return gravite; }
        @Override public void setAffecteeParGravite(boolean affecte) { this.gravite = affecte; }
    }

    @Test
    public void testGraviteAppliqueeCorrectement() {
        Gravite gravite = new Gravite(9.8f, 50f);
        FakeEntite entite = new FakeEntite();
        entite.setVitesseY(0f);

        gravite.appliquer(entite, 1.0f); // 1 seconde écoulée

        assertEquals(9.8f, entite.getVitesseY(), 0.001f);
    }

    @Test
    public void testGraviteRespecteVitesseMax() {
        Gravite gravite = new Gravite(9.8f, 20f);
        FakeEntite entite = new FakeEntite();
        entite.setVitesseY(18f);

        gravite.appliquer(entite, 1.0f); // Cela donnerait 27.8f sans limitation

        assertEquals(20f, entite.getVitesseY(), 0.001f);
    }

    @Test
    public void testGraviteNonAppliqueeSiNonAffectee() {
        Gravite gravite = new Gravite(9.8f, 50f);
        FakeEntite entite = new FakeEntite();
        entite.setAffecteeParGravite(false);
        entite.setVitesseY(5f);

        gravite.appliquer(entite, 1.0f);

        assertEquals(5f, entite.getVitesseY(), 0.001f);
    }
}
