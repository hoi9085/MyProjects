package back;

/** Obstacle modélise un obstacle dans le plateau qui gene l'avancement des joueurs.  
 *
 */

public class Obstacle {
	
    // Attributs
    private int positionX;
    private int positionY;

	public Obstacle(int vPositionX, int vPositionY) {
		//assert dans le plateau
		this.positionX = vPositionX;
		this.positionY = vPositionY;
	}

	public int getPositionX() {
        return this.positionX;
    }

    public void setPositionX(int positionX) {
        this.positionX = positionX;
    }

    public int getPositionY() {
        return this.positionY;
    }

    public void setPositionY(int positionY) {
        this.positionY = positionY;
    }
	
}