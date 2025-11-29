import numpy as np
import random
import os
from collections import deque

# Les mouvements possible quand on fixe un petit cube

def Left_Prime(pos):
    new_pos = pos.copy()
    new_pos[3][2] = pos[5][0]
    new_pos[3][3] = pos[5][1]
    new_pos[0][2] = pos[3][2]
    new_pos[0][3] = pos[3][3]
    new_pos[2][2] = pos[0][2]
    new_pos[2][3] = pos[0][3]
    new_pos[5][0] = pos[2][2]
    new_pos[5][1] = pos[2][3]
    new_pos[1][3] = pos[1][0]
    new_pos[1][0] = pos[1][1]
    new_pos[1][1] = pos[1][2]
    new_pos[1][2] = pos[1][3]
    return new_pos


def Down_Prime(pos):
    new_pos = pos.copy()
    new_pos[3][1] = pos[4][0]
    new_pos[3][2] = pos[4][1]
    new_pos[4][0] = pos[2][3]
    new_pos[4][1] = pos[2][0]
    new_pos[2][0] = pos[1][3]
    new_pos[2][3] = pos[1][2]
    new_pos[1][3] = pos[3][2]
    new_pos[1][2] = pos[3][1]
    new_pos[5][0] = pos[5][1]
    new_pos[5][1] = pos[5][2]
    new_pos[5][2] = pos[5][3]
    new_pos[5][3] = pos[5][0]
    return new_pos


def Back_Prime(pos):
    new_pos = pos.copy()
    new_pos[4][3] = pos[0][3]
    new_pos[4][0] = pos[0][0]
    new_pos[0][0] = pos[1][0]
    new_pos[0][3] = pos[1][3]
    new_pos[1][0] = pos[5][0]
    new_pos[1][3] = pos[5][3]
    new_pos[5][0] = pos[4][0]
    new_pos[5][3] = pos[4][3]
    new_pos[2][0] = pos[2][1]
    new_pos[2][1] = pos[2][2]
    new_pos[2][2] = pos[2][3]
    new_pos[2][3] = pos[2][0]
    return new_pos


def Left(pos):
    new_pos = pos.copy()
    new_pos[5][0] = pos[3][2]
    new_pos[5][1] = pos[3][3]
    new_pos[3][2] = pos[0][2]
    new_pos[3][3] = pos[0][3]
    new_pos[0][2] = pos[2][2]
    new_pos[0][3] = pos[2][3]
    new_pos[2][2] = pos[5][0]
    new_pos[2][3] = pos[5][1]
    new_pos[1][0] = pos[1][3]
    new_pos[1][1] = pos[1][0]
    new_pos[1][2] = pos[1][1]
    new_pos[1][3] = pos[1][2]
    return new_pos


def Down(pos):
    new_pos = pos.copy()
    new_pos[4][0] = pos[3][1]
    new_pos[4][1] = pos[3][2]
    new_pos[2][3] = pos[4][0]
    new_pos[2][0] = pos[4][1]
    new_pos[1][3] = pos[2][0]
    new_pos[1][2] = pos[2][3]
    new_pos[3][2] = pos[1][3]
    new_pos[3][1] = pos[1][2]
    new_pos[5][1] = pos[5][0]
    new_pos[5][2] = pos[5][1]
    new_pos[5][3] = pos[5][2]
    new_pos[5][0] = pos[5][3]
    return new_pos


def Back(pos):
    new_pos = pos.copy()
    new_pos[0][3] = pos[4][3]
    new_pos[0][0] = pos[4][0]
    new_pos[1][0] = pos[0][0]
    new_pos[1][3] = pos[0][3]
    new_pos[5][0] = pos[1][0]
    new_pos[5][3] = pos[1][3]
    new_pos[4][0] = pos[5][0]
    new_pos[4][3] = pos[5][3]
    new_pos[2][1] = pos[2][0]
    new_pos[2][2] = pos[2][1]
    new_pos[2][3] = pos[2][2]
    new_pos[2][0] = pos[2][3]
    return new_pos


# Liste des mouvements, sera utile durant la résolution
Adj = [Left, Left_Prime, Down, Down_Prime, Back, Back_Prime]


# Reverse_id pour pouvoir remettre la liste de recherche par le bas dans le bon ordre
Reverse_id = {0 : 1,
              1 : 0,
              2 : 3,
              3 : 2,
              4 : 5,
              5 : 4}


# Recherche bidirectionnelle en fixant un petit cube
def bidirectional_solve(start_pos, end_pos, max_depth):
    # Comparaison de nos positions initiale et finale, pour vérifier une égalité éventuelle, et donc que nous sommes déjà dans un état résolu
    if (start_pos == end_pos).all():
        return []
    
    # Initialisation des files pour la recherche en avant et en arrière
    forward_queue = deque([(start_pos, [])])
    backward_queue = deque([(end_pos, [])])
    # Initialisation des dictionnaires pour suivre les positions visitées
    forward_visited = {tuple(map(tuple, start_pos)): []}
    backward_visited = {tuple(map(tuple, end_pos)): []}
    
    # Boucle principale de la recherche bidirectionnelle
    while forward_queue and backward_queue:
        # Exploration de positions à partir de la position initial (start_pos)
        current_cube, current_moves = forward_queue.popleft()
        # Pour vérifier si on dépasse la profondeur maximale (6)
        if len(current_moves) >= max_depth:
            continue
        # Exploration des voisins (par mouvements) de la position actuelle
        for i in range(len(Adj)):
            new_cube = Adj[i](current_cube)
            new_hashable_cube = tuple(map(tuple, new_cube))
            # Vérification d'une visite de la position actuelle
            if new_hashable_cube not in forward_visited:
                # Mise à jour du dictionnaire et de la file
                forward_visited[new_hashable_cube] = current_moves + [Adj[i]]
                forward_queue.append((new_cube, current_moves + [Adj[i]]))

                # Recherche d'intersection avant la recherche en arrière
                if new_hashable_cube in backward_visited:
                    backward_visited[new_hashable_cube].reverse()
                    return forward_visited[new_hashable_cube] + backward_visited[new_hashable_cube]

        # Exploration de positions à partir de la solution (end_pos), même idée qu'avant
        current_cube, current_moves = backward_queue.popleft()
        if len(current_moves) >= max_depth:
            continue
        for i in range(len(Adj)):
            new_cube = Adj[i](current_cube)
            new_hashable_cube = tuple(map(tuple, new_cube))
            if new_hashable_cube not in backward_visited:
                backward_visited[new_hashable_cube] = current_moves + [Adj[Reverse_id[i]]]
                backward_queue.append((new_cube, current_moves + [Adj[Reverse_id[i]]]))
                # Recherche d'intersection
                if new_hashable_cube in forward_visited:
                    backward_visited[new_hashable_cube].reverse()
                    return forward_visited[new_hashable_cube] + backward_visited[new_hashable_cube]
    # Si aucune intersection n'est trouvée, on n'a donc pas une solution, on retourne None
    return None


# c'est une fonction pour nous aider à impmrimer les mouvements en lettres, et pour faciliter leur
# manipulation dans le code de l'interface 3D, qui reprend les mouvements différemment pour le cube
def fcte_to_lettres(list):
    if not list:
        return []
    for i in range(len(list)):
        if list[i] == Left_Prime:
            list[i] = "L'"
        if list[i] == Left:
            list[i] = "L"
        if list[i] == Down_Prime:
            list[i] = "D'"
        if list[i] == Down:
            list[i] = "D"
        if list[i] == Back_Prime:
            list[i] = "B'"
        if list[i] == Back:
            list[i] = "B"
    return list


def is_resolved(pos): # fonction pour vérifier si notre état actuel est notre état final, et donc que le cube est résolu
    for face in pos:
        if len(set(face)) != 1:
            return False
    return True


# Create solved cube position
solved_pos = np.array([['W', 'W', 'W', 'W'],
                       ['G', 'G', 'G', 'G'],
                       ['P', 'P', 'P', 'P'],
                       ['R', 'R', 'R', 'R'],
                       ['B', 'B', 'B', 'B'],
                       ['Y', 'Y', 'Y', 'Y']])
