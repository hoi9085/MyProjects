# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#Question 12:
from itertools import product
import random
import play
import codebreaker3
import codemaker2
import common 


def init():
    global comb_poss  # Variable globale pour stocker toutes les combinaisons
    
    # Initialisation de cette variable en générant toutes les combinaisons possibles
    comb_poss = ["".join(combinaison) for combinaison in product(common.COLORS, repeat=common.LENGTH)]
    
    # Variable globale pour stocker l'ensemble des combinaisons encore valides, elle change au fur et à mesure
    global possibles_encore
    possibles_encore = ["".join(combinaison) for combinaison in product(common.COLORS, repeat=common.LENGTH)]
    
    # Variable globale pour stocker le dernier choix
    global dernier_choix
    
    # Variable globale pour stocker l'ensemble des évaluations possibles
    global evaluation_possibles
    evaluation_possibles = common.evaluation_possibles(common.LENGTH)
    
    # Initialisation du dernier choix à None
    dernier_choix = None


def codebreaker(evaluation_p):
    global comb_poss
    global evaluation_possibles
    global possibles_encore
    global dernier_choix
    
    if evaluation_p == None:
        # Si c'est le premier coup, choisir la meilleure combinaison arbitrairement
        dernier_choix = common.meilleur_choix(common.LENGTH, possibles_encore, evaluation_possibles, comb_poss)
    else:
        # Mettre à jour l'univers après le dernier essai
        common.maj_possibles(possibles_encore, dernier_choix, evaluation_p)
        
        # Choisir la meilleure combinaison parmi les restantes
        dernier_choix = common.meilleur_choix(common.LENGTH, possibles_encore, evaluation_possibles, comb_poss)
    
    return dernier_choix

