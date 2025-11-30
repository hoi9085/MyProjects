package back;
/**
 * Gère les calculs liés à la gravité pour les entités du jeu.
 */
public class Gravite {
    // Intensité de la gravité (pixels par seconde²)
    private final float intensiteGravite;

    // Vitesse maximale de chute
    private final float vitesseMaxChute;

    /**
     * Crée une gravité avec une intensité donnée.
     * 
     * @param intensiteGravite Accélération due à la gravité
     * @param vitesseMaxChute Vitesse de chute maximale
     */
    public Gravite(float intensiteGravite, float vitesseMaxChute) {
        this.intensiteGravite = intensiteGravite;
        this.vitesseMaxChute = vitesseMaxChute;
    }

    /**
     * Applique la gravité à une entité.
     * 
     * @param entite L'entité affectée par la gravité
     * @param deltaTemps Temps écoulé depuis la dernière mise à jour (en secondes)
     */
    public void appliquer(EntitePhysique entite, float deltaTemps) {
        if (!entite.estAffecteeParGravite()) return;

        float nouvelleVitesseY = entite.getVitesseY() + intensiteGravite * deltaTemps;
        if (nouvelleVitesseY > vitesseMaxChute) {
            nouvelleVitesseY = vitesseMaxChute;
        }
        entite.setVitesseY(nouvelleVitesseY);
    }
}