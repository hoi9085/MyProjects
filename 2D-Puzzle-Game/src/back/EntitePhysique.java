package back;

/**
 * Interface représentant une entité affectée par les lois physiques du jeu.
 */
public interface EntitePhysique {
    /**
     * Obtient la vitesse horizontale de l'entité.
     * 
     * @return La vitesse horizontale (en pixels par seconde)
     */
    float getVitesseX();
    
    /**
     * Obtient la vitesse verticale de l'entité.
     * 
     * @return La vitesse verticale (en pixels par seconde)
     */
    float getVitesseY();
    
    /**
     * Définit la vitesse horizontale de l'entité.
     * 
     * @param vx Nouvelle vitesse horizontale (en pixels par seconde)
     */
    void setVitesseX(float vx);
    
    /**
     * Définit la vitesse verticale de l'entité.
     * 
     * @param vy Nouvelle vitesse verticale (en pixels par seconde)
     */
    void setVitesseY(float vy);
    
    /**
     * Indique si l'entité est affectée par la gravité.
     * 
     * @return true si l'entité est affectée par la gravité, false sinon
     */
    boolean estAffecteeParGravite();
    
    /**
     * Définit si l'entité est affectée par la gravité.
     * 
     * @param affecte true si l'entité doit être affectée par la gravité, false sinon
     */
    void setAffecteeParGravite(boolean affecte);
}