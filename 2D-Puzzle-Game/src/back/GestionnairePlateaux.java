package back;
//classe pour gerer le passage d'un niveau a l'autre, (à supprimer plus tard si on en a pas besoin)

public class GestionnairePlateaux {
    private Plateau niveauActuel;  // niveau actuellement actif

    // charger un niveau donné
    public Plateau chargerNiveau(int numeroNiveau) {
        switch (numeroNiveau) {
            case 1:
                niveauActuel = new Plateau1();
                break;
            case 2:
                niveauActuel = new Plateau2(); // niveau2 à definir 
                break;
            case 3:
                niveauActuel = new Plateau3(); // niveau3 à definir 
                break;
            default:
                return null; // ou un écran de fin
        }
        return (Plateau) niveauActuel;
    }

    //obtenir le plateau actuel
    public Plateau getPlateauActuel() {
        return (Plateau) niveauActuel;
    }
}

