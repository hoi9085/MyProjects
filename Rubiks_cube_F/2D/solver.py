import numpy as np
from collections import deque

#Les mouvements possibles quand on fixe un petit cube

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



def verification(M):
    """
    Verifie de la validite de la configuration representee par M
    """
    z=0
    d=[]
    s=[]
    a=[(3, 5, 1),
       (4, 5, 3),
       (1, 0, 3),
       (4, 0, 2),
       (2, 5, 4),
       (0, 4, 3),
       (5, 2, 1),
       (1, 2, 0)]

    b=[(3, 5, 1),
       (4, 5, 3),
       (1, 0, 3),
       (4, 0, 2),
       (2, 5, 4),
       (0, 4, 3),
       (5, 2, 1),
       (1, 2, 0),#
       (1, 3, 5),
       (3, 4, 5),
       (3, 1, 0),
       (2, 4, 0),
       (5, 4, 2),
       (4, 3, 0),
       (2, 1, 5),
       (2, 0, 1),#
       (5, 1, 3), 
       (5, 3, 4),
       (0, 3, 1),
       (0, 2, 4),
       (4, 2, 5),
       (3, 0, 4),
       (1, 5, 2),
       (0, 1, 2)]
    
    orientationsassociées={
       (3, 5, 1):0,
       (4, 5, 3):1,
       (1, 0, 3):1,
       (4, 0, 2):1,
       (2, 5, 4):0,
       (0, 4, 3):1,
       (5, 2, 1):2,
       (1, 2, 0):2,#
       (1, 3, 5):2,
       (3, 4, 5):0,
       (3, 1, 0):0,
       (2, 4, 0):0,
       (5, 4, 2):1,
       (4, 3, 0):2,
       (2, 1, 5):0,
       (2, 0, 1):0,#
       (5, 1, 3):1, 
       (5, 3, 4):2,
       (0, 3, 1):2,
       (0, 2, 4):2,
       (4, 2, 5):2,
       (3, 0, 4):0,
       (1, 5, 2):1,
       (0, 1, 2):1}
    
    d1=[[0,2], [3,3], [1,1],  # up,left,front
       [0, 0], [2, 1], [4, 3],  # behind,up,right
       [0, 3], [1, 0] , [2, 2],  # behind,left,up
       [0, 1], [4, 2], [3, 0],  # front,up,right
       [5, 0], [2, 3], [1, 3],  # down,left,behind
       [5, 1], [1, 2], [3, 2],  # front,left,down
       [5, 3], [4, 0], [2, 0],  # down,behind,right
       [5, 2] ,[3, 1], [4, 1]]  # front,down,right 
    
    for i in range(len(d1)):
        k=d1[i]
        s.append(M[k[0]][k[1]])
    for i in range(8):
        d.append((s[i*3], s[i*3+1], s[i*3+2]))
    z=0
    k=0
    nombre=0
    for j in range(8):
        for h in range(8):
            if d[h][0] in a[j] and d[h][1] in a[j] and d[h][2] in a[j] :
                z+=1
    if z == 8:
       for j in range (24) :
           for h in range (8):
               if d[h] == b[j] :
                   k+=1
                   nombre+=(orientationsassociées[d[h]])
    else:
        return False
    if k==8 and nombre%3==0 :
        return True
    else : 
        return False
    
    
def solve(start_pos):
    """
    Calule la solution optimale pour la configuration start_pos
    """
    end_pos = np.empty((6,4), dtype=int)
    for x in range(6):
        for y in range(4):
            end_pos[x,y] = x
            
    max_depth = 6
    forward_queue = deque([(start_pos, [])])
    backward_queue = deque([(end_pos, [])])
    forward_visited = {tuple(map(tuple, start_pos)): []}
    backward_visited = {tuple(map(tuple, end_pos)): []}
    
    if forward_visited == backward_visited:
        return []

    while forward_queue and backward_queue:
        # Exploration de positions à partir de la position initial (start_pos)
        current_cube, current_moves = forward_queue.popleft()
        if len(current_moves) >= max_depth:
            continue
        for i in range(len(MOVEMENTS)):
            new_cube = MOVEMENTS[i](current_cube)
            new_hashable_cube = tuple(map(tuple, new_cube))
            if new_hashable_cube not in forward_visited:
                forward_visited[new_hashable_cube] = current_moves + [i]
                forward_queue.append((new_cube, current_moves + [i]))

                # Recherche d'intersection
                if new_hashable_cube in backward_visited:
                    backward_visited[new_hashable_cube].reverse()
                    return forward_visited[new_hashable_cube] + backward_visited[new_hashable_cube]

        # Exploration de positions à partir de la solution (end_pos)
        current_cube, current_moves = backward_queue.popleft()
        if len(current_moves) >= max_depth:
            continue
        for i in range(len(MOVEMENTS)):
            new_cube = MOVEMENTS[i](current_cube)
            new_hashable_cube = tuple(map(tuple, new_cube))
            if new_hashable_cube not in backward_visited:
                backward_visited[new_hashable_cube] = current_moves + [Reverse_id[i]]
                backward_queue.append((new_cube, current_moves + [Reverse_id[i]]))
                # Recherche d'intersection
                if new_hashable_cube in forward_visited:
                    backward_visited[new_hashable_cube].reverse()
                    return forward_visited[new_hashable_cube] + backward_visited[new_hashable_cube]

    return None

MOVEMENTS = (Left, Left_Prime, Down, Down_Prime, Back, Back_Prime)

#Reverse_id pour pouvoir remettre la liste de recherche par le bas dans le bon ordre
Reverse_id = {0 : 1,
              1 : 0,
              2 : 3,
              3 : 2,
              4 : 5,
              5 : 4}

