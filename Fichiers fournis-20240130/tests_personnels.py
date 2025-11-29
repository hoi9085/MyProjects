#%%
# Question 1
import common

# Combinaisons choisies
c1 = 'RVVR'
c2 = 'RBOG'
c3 = 'JNMN'
c4 = 'OMRJ'
c5 = 'RRRR'
c = [c1, c2, c3, c4, c5]

# Combinaisons de référence choisies
cr1 = 'RVBJ'
cr2 = 'NOMG'
cr3 = 'NNOM'
cr4 = 'RVBJ'
cr5 = 'BRRJ'
cr = [cr1, cr2, cr3, cr4, cr5]

resultat = []

assert len(c) == len(cr) # Si on veut rajouter plus de tests

#Evaluations
for i in range(len(c)):
    tot_eval = common.evaluation(c[i], cr[i])
    print("évaluation ({}, {}) : {}".format(c[i], cr[i], tot_eval))
# affiche : évaluation (RVVR, RVBJ) : (2, 0)
#           évaluation (RBOG, NOMG) : (1, 1)
#           évaluation (JNMN, NNOM) : (1, 2)
#           évaluation (OMRJ, RVBJ) : (1, 1)
#           évaluation (RRRR, BRRJ) : (2, 0)

#%%
# Question 10
import codemaker2
import codemaker1
import codebreaker2
import play
import check_codemaker


play.play_log(codemaker2, codebreaker2, 'log0.txt', True)
print(check_codemaker.check_codemaker('log0.txt'))

play.play_log(codemaker1, codebreaker2, 'log0.txt', True)
print(check_codemaker.check_codemaker('log0.txt'))

# Les deux affichent que le codemaker n'a pas triché, ce qui est complètement logique