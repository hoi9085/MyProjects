#!/usr/bin/env python3

import common


def play(codemaker, codebreaker, quiet=False):
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