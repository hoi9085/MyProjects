#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:32:19 2024

@author: fred
"""

#%%
import tkinter as tk
import random
import numpy as np
import display_sol
import solver
import reco

fen = tk.Tk()
fen.geometry("1000x600")


class Box:
    # representation graphique d une facette. Possede donc une position et une couleur. 
    global config, btns_pos, colors_count

    def __init__(self, pos, color):
        """
        Parameters
        ----------
        pos : int
            code la position de la facette dans le patron sous forme d un int dans [0;23]
        color : int
            code la couleur associee a la facette (6 pour grey a l initialisation)
        ----------
        cree les facettes sur le patron
        """
        self.pos = pos
        self.color = color
        self.x, self.y = btns_pos[pos//4][pos%4]
        # creation d un carre pour representer la facette :
        self.rect = tk.Label(cube_can, width=4, height=2, bg=COLORS_BIND[color], borderwidth=2, relief='groove')
        self.rect.grid(row=self.x, column=self.y)

    def initHandselect(self):
        """
        ajoute un bouton sur chaque facette pour lui associer une couleur
        """
        fixed = (1, 12, 18) # positions fixees (Bleu-Blanc-Rouge)
        if self.pos not in fixed:
            self.activateBtn = tk.Button(cube_can, width=2, height=2, command=self.displayColorChoice)
            self.activateBtn.grid(row=self.x, column=self.y)

    def displayColorChoice(self):
        """
        affiche la liste des boutons pour les couleurs encore attribuables
        """
        self.activateBtn.config(text='X') # quand une facette est selectionnee
        self.cc_desc = tk.Label(cc_can, text='Choisir une couleur')
        self.cc_desc.pack(side=tk.TOP)
        self.btncc_list=[]
        for color in range(6):
            if colors_count[color] < 4: # verifie si la couleur est encore attribuable
                btn = tk.Button(cc_can, text=COLORS_BIND[color], command=lambda c=color : self.bindColor(c, hand_selec=True))
                self.btncc_list.append(btn)
                btn.pack(side=tk.TOP)

    def bindColor(self, newcolor, hand_selec=False):
        """
        Parameters
        ----------
        newcolor : int
            code la nouvelle couleur a associer a la facette
        hand_selec : Bool
            True si le mode de remplissage est a la main, False sinon
        ----------
        modifie la couleur associee a la facette
        """
        emptyboxes_alert.pack_forget()
        invalidcube_alert.pack_forget()
        if hand_selec: # detruire les boutons de choix de couleur a chaque fois
            self.activateBtn.destroy()
            self.cc_desc.destroy()
            for btncc in self.btncc_list:
                btncc.destroy()
                
        config[self.pos//4][self.pos%4] = newcolor # MAJ de la conig
        colors_count[newcolor] += 1
        self.rect.config(bg=COLORS_BIND[newcolor]) # MAJ de l affichage
        self.color = newcolor
        
            
def runRandom():
    """
    Effectue N=11 mouvements aleatoire a partir d un cube resolu et MAJ la config 
    """
    rand_btn.pack_forget()
    handselect_btn.pack_forget()
    reco_btn.pack_forget()
    
    # construction d un cube resolu
    config = np.empty((6,4), dtype=int)
    for x in range(6):
        for y in range(4):
            config[x,y] = x
    
    # modification pour avoir une config pseudo random
    N = 11
    for i in range(N):
        move = random.choice(solver.MOVEMENTS)
        config = move(config)
        
    for b in range(24):
        color = config[b//4][b%4]
        boxes[b].bindColor(color)

def runHandselect():
    """
    Inititalise la selection a la main
    """
    global cc_can
    
    rand_btn.pack_forget()
    handselect_btn.pack_forget()
    reco_btn.pack_forget()
    cc_can = tk.Canvas(fen)
    cc_can.pack(side=tk.LEFT) 
   
    for box in boxes:
        box.initHandselect()
        
def runReco():
    """
    Lance le programme de reconnaissance d image et MAJ la config
    """
    # recuperation de la config
    config = reco.main()
    for i in range(len(config)):
        for j in range(len(config[i])):
            config[i][j] = COLORS_BIND.index(config[i][j])
    print(config)
        
    rand_btn.pack_forget()
    handselect_btn.pack_forget()
    reco_btn.pack_forget()
    
    # MAJ graphique
    for b in range(24):
        color = config[b//4][b%4]
        boxes[b].bindColor(color)

        
def runSubmit():
    """
    Verifie la validite
    Si invalide : relance
    Si valide : calcule la solution et l affiche 
    """
    global resol_can 
    
    # Si facettes vides
    for face in config:
        if 6 in face:
            emptyboxes_alert.pack(side=tk.LEFT)
            return 
        
    # Si config invalide
    if not solver.verification(config):
        main()
        invalidcube_alert.pack(side=tk.LEFT)
        return 
        
    # Si config valide
    cube_can.delete('all')
    cube_can.configure(width=1300, height=800)
    submit_btn.pack_forget()
    cube_can.pack_forget()
    reco_btn.pack_forget()
    
    npconfig = np.array(config)
    print(npconfig)
    solution = solver.solve(npconfig) # calcul de la solution
    print(solution)
    replay_btn.pack(side=tk.TOP)
    cube_can.pack_forget()
    resol_can = tk.Canvas(fen, height=500, width=450)
    display_sol.displayAll(resol_can, solution, config) # affichage de la solution
    resol_can.pack(side=tk.LEFT)
    
    

def main():
    """
    Initialise la config et l affichage 
    """
    global boxes, config, colors_count
    
    # on initialise la config vide...
    config = [[6 for i in range(4)] for j in range(6)]
    # ...en fixant coin Bleu-Blanc-Rouge
    config[0][1] = 0
    config[3][0] = 3
    config[4][2] = 4
    colors_count = {0:1, 1:0, 2:0, 3:1, 4:1, 5:0}
    
    boxes = []
    for b in range(24):
        box = Box(b, config[b//4][b%4])
        boxes.append(box)
        
    cube_can.pack(side=tk.LEFT)
    btns_can.pack(side=tk.RIGHT)
    rand_btn.pack(side=tk.RIGHT)
    handselect_btn.pack(side=tk.RIGHT)
    reco_btn.pack(side=tk.RIGHT)
    submit_btn.pack(side=tk.BOTTOM)

def replay():
    """
    Reinitialise tout
    """
    global resol_can
    replay_btn.pack_forget()
    resol_can.destroy()
    main()
    
COLORS_BIND = ('white', 'green', 'purple', 'red', 'blue', 'yellow', 'grey') # association entiers/couleurs

btns_pos = [[(2,3), (3,3), (3,2), (2,2)], # up
           [(2,1), (3,1), (3,0), (2,0)], # left
           [(0,3), (1,3), (1,2), (0,2)], # back
           [(4,3), (5,3), (5,2), (4,2)], # front
           [(2,5), (3,5), (3,4), (2,4)], # right
           [(2,7), (3,7), (3,6), (2,6)]] # down
    
# Definition des canvas, boutons et alertes 

cube_can = tk.Canvas(fen, bg='white', height=500, width=450)
btns_can = tk.Canvas(fen, bg='white', height=500, width=450)

rand_btn = tk.Button(btns_can, text='Random', command=runRandom)
handselect_btn = tk.Button(btns_can, text='Manuel', command=runHandselect)
reco_btn = tk.Button(btns_can, text='Photo', command=runReco)
submit_btn = tk.Button(btns_can, text='Submit', command=runSubmit)
replay_btn = tk.Button(btns_can, text='Replay', command=replay)

emptyboxes_alert = tk.Label(fen, text='Facettes vides')
invalidcube_alert = tk.Label(fen, text='Config non valide')

main()
tk.mainloop()
