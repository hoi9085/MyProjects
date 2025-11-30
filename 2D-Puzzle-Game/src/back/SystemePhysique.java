package back;

/**
 * Système de gestion de la gravité
 */
public class SystemePhysique {
    private final Gravite gravite;

    /**
     * Initialise le système physique avec la gravité.
     * 
     * @param intensiteGravite Intensité de la gravité
     * @param vitesseMaxChute Vitesse maximale de chute
     */
    public SystemePhysique(float intensiteGravite, float vitesseMaxChute) {
        this.gravite = new Gravite(intensiteGravite, vitesseMaxChute);
    }

    /**
     * Met à jour la gravité sur une entité.
     * 
     * @param entite L'entité à mettre à jour
     * @param deltaTemps Temps écoulé depuis la dernière mise à jour (en secondes)
     */
    public void mettreAJour(EntitePhysique entite, float deltaTemps) {
        gravite.appliquer(entite, deltaTemps);
    }
}

