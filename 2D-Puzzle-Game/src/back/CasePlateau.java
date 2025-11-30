package back;


public class CasePlateau {
    public enum TypeCase {
        VIDE, MUR, JOUEUR1, JOUEUR2, BARRIL, CIBLE, CLEF, LAVE, PIQUE, POMME, PORTE_FERMEE, PORTE_OUVERTE, ETOILE, COEUR, VIE, VIE0, VIE1, VIE2, VIE3;
    }

    private boolean obstruant;
    private boolean danger;
    private TypeCase type;
    private int positionX;
    private int positionY;

    public CasePlateau(TypeCase type, int vPositionX, int vPositionY) {
        this.type = type;
        this.positionX = vPositionX;
		this.positionY = vPositionY;
        if (type == TypeCase.MUR || type == TypeCase.BARRIL || type == TypeCase.CIBLE){
            obstruant = true;
        }else{
            obstruant = false;
        }
        if (type == TypeCase.PIQUE || type == TypeCase.LAVE){
            danger = true;
        }else{
            danger = false;
        }
    }

    public TypeCase getType() {
        return type;
    }

	public int getPositionX() {
        return this.positionX;
    }
    
    public int getPositionY() {
        return this.positionY;
    }

    public boolean estObstruant() {return this.obstruant;}
    
    public boolean estDanger() {return this.danger;}

    public void setPositionX(int positionX) {
        this.positionX = positionX;
    }

    public void setPositionY(int positionY) {
        this.positionY = positionY;
    }

    public void setObstruant(boolean obstruant) {
        this.obstruant = obstruant;
    }

    public void setDanger(boolean danger) {
        this.danger = danger;
    }
    
    public void setType(TypeCase type) {
        this.type = type;
    }
}
