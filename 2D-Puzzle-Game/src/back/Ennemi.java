package back;

public class Ennemi extends Personnage {
    private int degats;

    public Ennemi(String nom, int degats, int vie,  int positionX, int positionY) {
        super(nom, vie , positionX, positionY);
        this.degats = degats;
    }

    public int getDegats() {
        return degats;
    }

    public void attaquer(Personnage cible) {
        cible.subirDegats(degats);
    }
}
