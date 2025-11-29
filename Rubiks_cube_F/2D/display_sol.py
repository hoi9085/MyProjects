#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:25:02 2024

@author: fred
"""

import tkinter as tk
import numpy as np
import solver

def displayConfig(fen, config, sol_row, sol_col):
    """
    Parameters
    ----------
    fen : tk.Canvas
        canvas dans lequel on affiche la solution.
    config : matrice
        config intermediaire de la solution.
    sol_row : int
        ligne pour l affichage.
    sol_col : int
        colonne pour l affichage.
    ----------
    Affiche une configuration intermediaire de la solution
    """
    stepi_can = tk.Canvas(fen) # creation d un canvas pour chaque etape
    for f in range(6):
        for b in range(4):
            x, y = POS[f][b]
            c = COLORS[config[f][b]]
            box = tk.Label(stepi_can, bg=c, height=3, width=2, borderwidth=2, relief='groove')
            box.grid(row=x, column=y)
    stepi_can.grid(row=sol_row, column=sol_col, padx=10)
        
        
def displayAll(fen, moves_to_sol, config):
    """
    Parameters
    ----------
    fen : tk.Canvas
        canvas dans lequel on affiche la solution
    moves_to_sol : list d entiers
        chaque entier represente un mouvement
    config : matrice
        config initiale
    ----------
    affiche les etapes de la solution une par une et les mouvements pour y arriver
    """    
    displayConfig(fen, config, 1, 0)
    for mov_count, mov in enumerate(moves_to_sol): # pour chaque etape de la solution :
        config = np.array(solver.MOVEMENTS[mov](np.array(config))) # on MAJ la config
        name = tk.Label(fen, text=MOVEMENTS_BIND[mov])
        name.grid(row=2*(mov_count//5), column=2*(mov_count%5)+1) # on affiche le nom du mouvement
        displayConfig(fen, config, 2*(mov_count//5)+1, 2*(mov_count%5)+1) # et la config obtenue
        

# les positions des facettes sur le patron 2D, regroupees par faces

POS = [[(2,3), (3,3), (3,2), (2,2)], # up
       [(2,1), (3,1), (3,0), (2,0)], # left
       [(0,3), (1,3), (1,2), (0,2)], # back
       [(4,3), (5,3), (5,2), (4,2)], # front
       [(2,5), (3,5), (3,4), (2,4)], # right
       [(2,7), (3,7), (3,6), (2,6)]] # down

COLORS = ('white', 'green', 'purple', 'red', 'blue', 'yellow', 'grey')

           
MOVEMENTS_BIND = ['Left', 'Left_Prime', 'Down', 'Down_Prime', 'Back', 'Back_Prime'] # les noms des mouvements
