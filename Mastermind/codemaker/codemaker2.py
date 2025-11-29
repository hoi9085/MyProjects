import common
import random
from itertools import product
import codemaker2
import codebreaker2
import play
import matplotlib.pyplot as plt
import numpy as np


def init():
    global combinaison_cible, possibles_encore
    # Générer toutes les combinaisons possibles et les stocker dans possibles_encore
    l = {"".join(combination) for combination in product(common.COLORS, repeat=common.LENGTH)}
    possibles_encore = l
    # Choisir une combinaison aléatoire comme cible pour le premier tour
    combinaison_cible = ''.join(random.choices(common.COLORS, k=common.LENGTH))


def codemaker(proposition):
    global combinaison_cible, possibles_encore
    # Dictionnaire pour stocker le nombre de possibilités restantes pour chaque combinaison possible
    nombre_de_possibilites = {}
    # Parcours de toutes les combinaisons possibles restantes
    for combinaison in possibles_encore:
        # Évaluation de la proposition par rapport à chaque combinaison possible
        evaluation = common.evaluation(proposition, combinaison)
        # Mise à jour du nombre de possibilités restantes pour cette combinaison en fonction de l'évaluation
        nombre_de_possibilites[combinaison] = len(common.maj_possibles(possibles_encore.copy(), proposition, evaluation))
    # Ajustement de la combinaison cible en choisissant celle qui laisse le plus de possibilités restantes
    combinaison_cible = max(nombre_de_possibilites, key=nombre_de_possibilites.get)
    # Réévaluation de la proposition par rapport à la nouvelle combinaison cible
    evaluation = common.evaluation(proposition, combinaison_cible)
    # Mise à jour de la liste des combinaisons possibles en fonction de l'évaluation
    possibles_encore = common.maj_possibles(possibles_encore, proposition, evaluation)
    # Retourner l'évaluation pour informer le codebreaker
    return evaluation

