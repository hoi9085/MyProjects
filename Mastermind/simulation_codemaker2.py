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
    possibles_encore = {"".join(combination) for combination in product(common.COLORS, repeat=common.LENGTH)}
    combinaison_cible = None


def codemaker(proposition):
    global combinaison_cible, possibles_encore
    nouvelle_combinaison_cible = None
    max = 0
    for combinaison in possibles_encore:
        a = set(possibles_encore)
        evaluation = common.evaluation(proposition, combinaison)
        taille = len(common.maj_possibles(a, proposition, evaluation))
        if taille > max:
            max = taille
            nouvelle_combinaison_cible = combinaison
    # Ajustement de la combinaison cible en fonction de l'évaluation
    combinaison_cible = nouvelle_combinaison_cible
    evaluation = common.evaluation(proposition, combinaison_cible)
    possibles_encore = common.maj_possibles(possibles_encore, proposition, evaluation)
    return evaluation


nb_parties = 5
nb_essais = []
for i in range(nb_parties):
    nb_essais.append(play.play(untitled1, codebreaker2, quiet = True))
plt.hist(nb_essais, bins = 60)
plt.grid(True)
plt.show()
mean_attempts_simulated = np.mean(nb_essais)
print(mean_attempts_simulated)