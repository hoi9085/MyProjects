import common
from itertools import product

def check_codemaker(file):
    # Ouvrir le fichier de log en mode lecture
    with open(file, "r") as fichier:
        # Générer toutes les combinaisons possibles
        l = {"".join(combination) for combination in product(common.COLORS, repeat=common.LENGTH)}
        combinaisons_possibles = l
        while True:
            # Lire la proposition du fichier de log
            combinaison = fichier.readline().strip()
            if not combinaison:
                break
            # Vérifier si la proposition est une combinaison possible
            if combinaison not in combinaisons_possibles:
                print('Le codemaker a triché')
                return False
            # Lire l'évaluation du fichier de log
            string_evaluation = fichier.readline().strip()
            if string_evaluation:
                eval = tuple(map(int, string_evaluation.split(',')))
            else:
                print('Évaluation manquante pour la proposition {}'.format(combinaison))
                return False
            # Mettre à jour les combinaisons possibles en fonction de la proposition et de l'évaluation
            combinaisons_possibles = common.maj_possibles(combinaisons_possibles, combinaison, eval)
    print("Le codemaker n'a pas triché")
    return True
