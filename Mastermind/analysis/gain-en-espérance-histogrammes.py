import matplotlib.pyplot as plt
import codemaker1
import codebreaker1
import codebreaker0
import play
import numpy as np


nb_parties = 1000
nb_essais = []
nb_essais0 = []

for i in range(nb_parties):
    nb_essais.append(play.play(codemaker1, codebreaker1, quiet = True))
    nb_essais0.append(play.play(codemaker1, codebreaker0, quiet = True))
    
plt.hist([nb_essais, nb_essais0], bins = 50, label=['x', 'y'])
plt.legend(loc="upper left")
plt.grid(True)
plt.show()
mean_attempts_simulated = np.mean(nb_essais)
