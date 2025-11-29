import numpy as np
import random
import common
import play
import matplotlib.pyplot as plt
import codebreaker2
import codemaker1
from itertools import product


def init():
    global prev  # Utilisation de la variable globale prev pour suivre la combinaison précédente
    global possibles  # Utilisation de la variable globale possibles pour stocker les combinaisons possibles
    prev = None  # Initialisation de prev à None au début du jeu
    possibles = None  # Initialisation de possibles à None au début du jeu


def codebreaker(evaluation_p):
    global prev, possibles  # Utilisation des variables globales prev et possibles
    if evaluation_p is None:  # Si c'est le premier tour et aucune évaluation n'a été donnée
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))  # Générer une combinaison aléatoire
        prev = combinaison  # Mettre à jour prev avec la nouvelle combinaison
        return combinaison  # Retourner la combinaison
    if possibles is None:  # Si c'est le deuxième tour et aucune liste de combinaisons possibles n'a été générée
        possibles = common.donner_possibles(prev, evaluation_p)  # Trouver les combinaisons possibles en fonction de prev et evaluation_p
        combinaison = random.choice(list(possibles))  # Choisir aléatoirement une combinaison parmi les possibles
        prev = combinaison  # Mettre à jour prev avec la nouvelle combinaison
        return combinaison  # Retourner la combinaison
    possibles = common.maj_possibles(possibles, prev, evaluation_p)  # Mettre à jour la liste des combinaisons possibles en fonction de l'évaluation donnée
    combinaison = random.choice(list(possibles))  # Choisir aléatoirement une combinaison parmi les possibles restantes
    possibles.remove(combinaison)  # Retirer la combinaison choisie de la liste des possibles pour éviter de la choisir à nouveau
    prev = combinaison  # Mettre à jour prev avec la nouvelle combinaison
    return combinaison  # Retourner la combinaison

