#!/usr/bin/env python3

import common


def play(codemaker, codebreaker, quiet=False):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    Renvoie le nombre de coups joués pour trouver la solution

    Attention, il ne *doit* pas être nécessaire de modifier cette fonction 
    pour faire fonctionner vos codemaker et codebreaker (dans le cas contraire,
    ceux-ci ne seront pas considérés comme valables)
    """
    n_essais = 0
    codebreaker.init()
    codemaker.init()
    ev = None
    if not quiet:
        print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        combinaison = codebreaker.codebreaker(ev)
        ev = codemaker.codemaker(combinaison)
        n_essais += 1
        if not quiet:
            print("Essai {} : {} ({},{})".format(n_essais, combinaison, ev[0], ev[1]))
        if ev[0] >= common.LENGTH:
            if not quiet:
                print("Bravo ! Trouvé {} en {} essais".format(combinaison, n_essais))
            return n_essais


def play_log(codemaker, codebreaker, log_file, quiet):
    n_essais = 0
    # Initialisation des codemaker et codebreaker
    codebreaker.init()
    codemaker.init()
    ev = None
    # Ouverture du fichier de log en mode écriture
    with open(log_file, 'w') as file:
        # Affichage des informations sur la taille des combinaisons et les couleurs disponibles
        print('Combinaisons de taille {}, couleurs disponibles {}\n'.format(common.LENGTH, common.COLORS))
        while True:
            # Le codebreaker propose une combinaison en fonction de l'évaluation précédente
            combinaison = codebreaker.codebreaker(ev)
            # Le codemaker évalue la proposition du codebreaker et retourne le résultat
            ev = codemaker.codemaker(combinaison)
            n_essais += 1
            if not quiet:
                print("Essai {} : {} ({},{})".format(n_essais, combinaison, ev[0], ev[1]))
            # Écriture de la proposition dans le fichier de log
            file.write(combinaison + '\n')
            # Écriture de l'évaluation dans le fichier de log
            file.write("{},{}\n".format(ev[0], ev[1]))
            # Vérification si la combinaison a été trouvée
            if ev[0] >= common.LENGTH:
                if not quiet:
                    print("Bravo ! Trouvé {} en {} essais".format(combinaison, n_essais))
                # Retourne le nombre d'essais nécessaires pour trouver la combinaison
                return n_essais

"""
if __name__ == '__main__':
    # Les lignes suivantes sont à modifier / supprimer selon ce qu'on veut faire, quelques exemples :

    # Faire jouer ensemble codemaker0.py et codebreaker0.py pour 5 parties :
    import codebreaker0
    import codemaker0
    import codebreaker1
    import codemaker1
    for i in range(5):
        play(codemaker0, codebreaker1)

    #  Faire jouer un humain contre codemaker0.py :
    #import codemaker0
    #import human_codebreaker
    #play(codemaker0, human_codebreaker)

    # Et plus tard, vous pourrez faire jouer vos nouvelles version du codebreaker et codemaker :
    #import codebreaker2
    #import codemaker2
    #play(codemaker2, codebreaker2)

    # Ou encore :
    #import codebreaker1
    #import human_codemaker
    #play(human_codemaker, codebreaker1)
"""