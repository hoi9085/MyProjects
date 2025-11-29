#%%
#codebreaker0
import play
import numpy as np
import matplotlib.pyplot as plt
import codebreaker0
import codemaker1
import random
import common

# Nombre de parties à simuler
num_games = 10000

# Liste pour enregistrer le nombre d'essais nécessaires dans chaque partie
attempts_list = []

# Simulation des jeux
for _ in range(num_games):
    attempts = play.play(codemaker1, codebreaker0, quiet=True)
    attempts_list.append(attempts)

# Calcul de l'espérance à partir des données simulées
mean_attempts_simulated = np.mean(attempts_list)

# Affichage de l'histogramme
plt.hist(attempts_list, bins=50)
plt.title('Histogramme du nombre d\'essais nécessaires pour le codebreaker0')
plt.xlabel('Nombre d\'essais')
plt.ylabel('Nb de parties')
plt.grid(True)
plt.show()

print(mean_attempts_simulated)

#%%
#codebreaker1
import numpy as np
import random
import common
import play
import matplotlib.pyplot as plt
import codebreaker1
import codemaker1
from itertools import product

nb_parties = 1000
nb_essais = []
for i in range(nb_parties):
    nb_essais.append(play.play(codemaker1, codebreaker1, quiet = True))
plt.hist(nb_essais, bins = 80)
plt.title('Histogramme du nombre d\'essais nécessaires')
plt.xlabel('Nombre d\'essais')
plt.ylabel('Nb de parties')
plt.grid(True)
plt.show()
mean_attempts_simulated = np.mean(nb_essais)
print(mean_attempts_simulated)
#%%
#gain en espérance avec codebreaker1

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
    
plt.hist([nb_essais, nb_essais0], bins = 80, label=['codebreaker1', 'codebreaker0'])
plt.legend(loc="upper left")
plt.title('Histogramme du nombre d\'essais nécessaires')
plt.xlabel('Nombre d\'essais')
plt.ylabel('Nb de parties')
plt.grid(True)
plt.show()

#%%
#codebreaker2
import numpy as np
import random
import common
import play
import matplotlib.pyplot as plt
import codebreaker2
import codemaker1
from itertools import product

nb_parties = 2000
nb_essais = []
for i in range(nb_parties):
    nb_essais.append(play.play(codemaker1, codebreaker2, quiet = True))
plt.hist(nb_essais, bins = 15)
plt.grid(True)
plt.title('Histogramme du nombre d\'essais nécessaires pour le codebreaker2')
plt.xlabel('Nombre d\'essais')
plt.ylabel('Nb de parties')
plt.show()
mean_attempts_simulated = np.mean(nb_essais)
print(mean_attempts_simulated)

#%%
#comparaison codebreaker2 et codebreaker1

import matplotlib.pyplot as plt
import codemaker1
import codebreaker1
import codebreaker2
import play
import numpy as np


nb_parties = 1000
nb_essais = []
nb_essais1 = []

for i in range(nb_parties):
    nb_essais.append(play.play(codemaker1, codebreaker2, quiet = True))
    nb_essais1.append(play.play(codemaker1, codebreaker1, quiet = True))
    
plt.hist([nb_essais, nb_essais1], bins = 50, label=['codebreaker2', 'codebreaker1'])
plt.title('Histogramme du nombre d\'essais nécessaires')
plt.xlabel('Nombre d\'essais')
plt.ylabel('Nb de parties')
plt.legend(loc="upper left")
plt.grid(True)
plt.show()

#%%
#codemaker2
import common
import random
from itertools import product
import codemaker2
import codebreaker2
import play
import matplotlib.pyplot as plt
import numpy as np

nb_parties = 10
nb_essais = []
for i in range(nb_parties):
    nb_essais.append(play.play(codemaker2, codebreaker2, quiet = False))
plt.hist(nb_essais, bins = 15)
plt.title('Histogramme du nombre d\'essais nécessaires')
plt.xlabel('Nombre d\'essais')
plt.ylabel('Nb de parties')
plt.grid(True)
plt.show()
mean_attempts_simulated = np.mean(nb_essais)
print(mean_attempts_simulated)

#%%
#comparaison codemaker1 et codemaker2 vs codebreaker2
import common
import random
from itertools import product
import codemaker2
import codebreaker2
import codemaker1
import play
import matplotlib.pyplot as plt
import numpy as np

nb_parties = 10
nb_essais = []
nb_essais1 = []

for i in range(nb_parties):
    nb_essais.append(play.play(codemaker2, codebreaker2, quiet = False))
    nb_essais1.append(play.play(codemaker1, codebreaker2, quiet=False))

plt.hist([nb_essais1, nb_essais], bins = 15, label=['codemaker1', 'codemaker2'])
plt.title('Histogramme du nombre d\'essais nécessaires')
plt.xlabel('Nombre d\'essais')
plt.ylabel('Nb de parties')
plt.legend()
plt.grid(True)
plt.show()

#%%
#codebreaker3 comparaison codemaker1 et codemaker2
import time
from itertools import product
import random
import play
import codebreaker3
import codemaker1
import codemaker2
import common
import matplotlib.pyplot as plt

nb_essais1 = []
nb_essais2 = []
temps1 = []
temps2 = []

COLORS = ['R', 'V', 'B', 'J', 'N', 'O', 'M', 'G']


for i in range(4, 9, 1):
    common.COLORS = COLORS[:i].copy()
    print(common.COLORS)
    debut = time.perf_counter()
    a = play.play(codemaker1, codebreaker3, quiet=False)
    print('a =', a)
    fin = time.perf_counter_ns()
    nb_essais1.append(a)
    temps1.append(fin-debut)
    
    debut = time.perf_counter()
    b = play.play(codemaker2, codebreaker3, quiet=False)
    print('b =', b)
    fin = time.perf_counter_ns()
    nb_essais2.append(b)
    temps2.append(fin-debut)

print(nb_essais1)
print(nb_essais2)

common.COLORS = COLORS

i = [4, 5, 6, 7, 8]

plt.plot(i, nb_essais1, label='codemaker1')
plt.plot(i, nb_essais2, label='codemaker2')
plt.xlabel("nombre de couleurs")
plt.ylabel("nombre de fois obtenus")
plt.legend()
plt.grid(True)
plt.show()

plt.plot(i, temps1, label='codemaker1')
plt.plot(i, temps2, label='codemaker2')
plt.xlabel('nombre de couleurs')
plt.ylabel("temps du jeu")
plt.legend()
plt.grid(True)
plt.show()
