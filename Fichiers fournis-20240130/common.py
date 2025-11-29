#!/usr/bin/env python3
import random
from itertools import product
import copy 
LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'O', 'M', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus

#Question 1
def evaluation(combinaison, combinaison_reference):
    bien_places, mal_places = 0, 0 # Initialisation des compteurs
    combinaison1, combinaison2 = [], [] # Initialisation des lisltes qui vont contenir des éléments des combinaisons

    for i in range(len(combinaison)): # Boucle pour comparer chaque élément des combinaisons (et pour identifier les plots bien placés)
        if combinaison[i] == combinaison_reference[i]: # Les 2 éléments sont identiques dans la même place
            bien_places += 1  # Ajouter le nombre de plots bien placés
        else:
            combinaison1.append(combinaison_reference[i])  # Ajouter à combinaison1 si pas bien placé
            combinaison2.append(combinaison[i])  # Ajouter à combinaison2 si pas bien placé

    for e in combinaison2: # Parcourir les éléments non bien placés dans combinaison2 (pour identifier les plots mal placés)
        if e in combinaison1:  # Vérifier s'il existe dans combinaison1
            mal_places += 1  # Ajouter le nombre de plots mal placés
            combinaison1.remove(e)  # Retirer l'élément de combinaison1 s'il est trouvé dans combinaison2

    return bien_places, mal_places  # Renvoyer le nombre de plots bien et mal placés, sous forme de tuple


l = ["".join(combination) for combination in product(COLORS, repeat=LENGTH)]


#Question 5
# Fonction pour déterminer les combinaisons possibles en fonction d'une évaluation donnée
def donner_possibles(combinaison_testee, evaluation_associee):
    comb_possibles = set()  # Créer un ensemble pour stocker les combinaisons possibles
    for combinaison_possible in l:  # Parcourir toutes les combinaisons possibles
        # Évaluation de la combinaison pour voir si elle est possible
        eval = evaluation(combinaison_possible, combinaison_testee)
        if eval == evaluation_associee:  # Si l'évaluation correspond à l'évaluation associée
            comb_possibles.add(combinaison_possible)  # Ajouter la combinaison à l'ensemble des combinaisons possibles
    return comb_possibles  # Retourner l'ensemble des combinaisons possibles


#Question 6
# Fonction pour mettre à jour les combinaisons possibles en fonction d'une évaluation donnée
def maj_possibles(combinaisons_possibles_encore, combinaison_testee, evaluation_associee):
    enlever = []  # Créer une liste pour stocker les combinaisons à enlever
    for combinaison in combinaisons_possibles_encore:  # Parcourir chaque combinaison possible restante
        eval = evaluation(combinaison, combinaison_testee)  # Évaluer la combinaison
        if eval != evaluation_associee:  # Si l'évaluation ne correspond pas à l'évaluation associée
            enlever.append(combinaison)  # Ajouter la combinaison à la liste des combinaisons à enlever
    for combinaison in enlever:  # Parcourir la liste des combinaisons à enlever
            combinaisons_possibles_encore.remove(combinaison)  # Supprimer la combinaison des combinaisons possibles restantes
    return combinaisons_possibles_encore  # Retourner l'ensemble mis à jour des combinaisons possibles restantes



# Fonction qui permet de donner l'ensemble des évaluations possibles :
def evaluation_possibles(n):
    """
    Cette fonction génère toutes les évaluations possibles pour une combinaison de longueur `n`.
    Elle retourne un ensemble d'évaluations.
    """
    evaluations_possibles = set()
    
    # Boucle pour générer toutes les évaluations possibles
    for k in range(0, n + 1):
        for i in range(0, k + 1):
            evaluation = (i, k - i)
            evaluations_possibles.add(evaluation)
    
    # On retire l'évaluation (n - 1, 1) car elle est toujours donnée si la combinaison est presque correcte
    evaluations_possibles.remove((n - 1, 1))
    return evaluations_possibles


# Fonction qui compte le nombre de combinaisons éliminées pour chaque choix et évaluation
def compteur_information(combinaison, ev, univers):
    """
    Cette fonction compte le nombre de combinaisons éliminées pour une combinaison et une évaluation données.
    Elle retourne le nombre total de combinaisons éliminées.
    """
    info = 0
    
    # Si tous les éléments sont bien placés, alors il ne reste qu'une seule combinaison
    if ev[0] == len(combinaison):
        info = len(univers) - 1
        return info
    else:
        # Parcours de toutes les combinaisons possibles pour calculer le nombre d'éliminations
        for c in univers.copy():
            cpt = evaluation(combinaison, c)
            bien_places, mal_places = cpt[0], cpt[1]
            if bien_places != ev[0] or mal_places != ev[1]:
                info += 1
        return info


# Fonction qui choisit le meilleur guess parmi l'univers des combinaisons
def meilleur_choix(l, possibles_encore, ev_poss, comb_poss):
    """
    Cette fonction choisit la meilleure combinaison parmi l'univers des combinaisons encore possibles.
    Elle retourne la meilleure combinaison.
    """
    # Si l'univers des combinaisons possibles ne contient qu'une seule combinaison, on la retourne immédiatement
    if len(possibles_encore) == 1:
        return possibles_encore.pop(0)
    
    n = len(comb_poss)
    max_info = 0
    max_ev = (0, 0)
    best_combinaison = possibles_encore.pop(0)
    possibles_encore.append(best_combinaison)
    
    # Parcours de toutes les combinaisons encore possibles pour choisir la meilleure
    for c in list(possibles_encore):
        min_info = n
        ev0 = None
        
        # Parcours de toutes les évaluations possibles pour chaque combinaison
        for ev in ev_poss:
            info = compteur_information(c, ev, possibles_encore)
            if info <= min_info:
                ev0 = ev
                min_info = info
        
        # Sélection de la combinaison avec le maximum d'informations éliminées
        if min_info >= max_info:
            max_ev = ev0
            max_info = min_info
            best_combinaison = c
    
    # Affichage pour le débogage ou l'analyse
    print("max_ev={} et max_info={}".format(max_ev, max_info))
    return best_combinaison

