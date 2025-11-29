import Bidirectional_solve_fonctionnel as bsf
from vpython import *
import numpy as np
import random
import detection_couleur_3D as dc
from vpython import vector, button, canvas, box, sphere, label, rate, sleep
class Rubic_Cube():
    
    def __init__(self):
        self.scene = canvas(width=1200, height=800)
        self.scene.caption = "Rubik's Cube Solver"
    
        self.en_marche = True
        self.carrés = [] 
        self.dAngle = np.pi/40 # UN ANGLE 
        self.values = []
        try:
            self.instruction = label(text="", pos=vector(0, 1.25, 1))
        except:
            self.instruction = None   # texte vide affiché en haut du rubiks cube
        #center
        sphere(pos=vector(0,0,0),size=vector(1,1,1),color=vector(0,0,0))# la sphère est positionnée
        #AU CENTRE DU RUBIKS CUBE
        # on va créer une liste de listes contenant les positions des carrés du Rubiks cube dans l'espace 3D
        #Chaque sous-liste représente une face du cube avec les positions des tuiles  représentées comme
        #des vecteurs 3D avec des coordonnées x, y et z.

        carré_pos = [[vector(0.5,1, -0.5), vector(0.5, 1, 0.5),          # top
                     vector(-0.5, 1, 0.5), vector(-0.5, 1, -0.5),
                     ],
                     [vector(-1, 0.5, -0.5), vector(-1, 0.5,0.5),          # left
                      vector(-1,-0.5, 0.5),vector(-1, -0.5, -0.5),
                      ],
                     [vector(0.5, -0.5, -1), vector(0.5, 0.5, -1),        # back
                      vector(-0.5, 0.5, -1), vector(-0.5, -0.5, -1),
                      ], 
                     [vector(0.5, 0.5, 1),vector(0.5, -0.5, 1),           #front
                     vector(-0.5, -0.5, 1),vector(-0.5,0.5 , 1),
                     ],
                    [vector(1, -0.5, -0.5),vector(1, -0.5, 0.5),         # right
                     vector(1, 0.5, 0.5),vector(1, 0.5, -0.5),
                     ],
                    [vector(-0.5, -1, -0.5),vector(-0.5, -1, 0.5),     # bottom
                    vector(0.5, -1, 0.5),vector(0.5, -1, -0.5), 
                     ],
                   ]


        # vecteurs représentant les couleurs des six faces du cube Rubik.
        colors = [
            vector(1, 1, 1),  # top (white)
            vector(0, 1, 0),  # left (green)
            vector(1, 0, 1),  # back (move)
            vector(1, 0, 0),  # front (red)
            vector(0, 0, 1),  # right (blue)
            vector(1, 1, 0),  # bottom (yellow)
        ]      
  
        #on va créer une liste de tuples représentant les angles de rotation et
        #les axes de rotation pour chaque face du cube.

        angle = [(np.pi/2,vector(1,0,0)), (np.pi/2,vector(0,1,0)), (0,vector(0,0,0)), (0,vector(0,0,0)), (np.pi/2,vector(0,1,0)), (np.pi/2,vector(1,0,0))]
        #on crée le rubiks cube :oriontation de la face top, left, back,front,right, bottom
        # vect(1,0,0) axe des x;  vect(0,1,0) axe des y; vect(0,0,1) axe des z
        #sides
        #on utilise une double boucle for pour créer des objets de type boîte (box)
        #en utilisant VPython. 
        #Ces boîtes représentent les carrés du cube  et sont positionnées
        #et colorées en fonction
        #des données fournies dans la liste carré_pos, la liste couleurs et la liste angle

        #sides
        for rank,side in enumerate(carré_pos):
            #rank représente l'indice de l'élément actuel dans la liste carré_pos.
           #side est la variable qui stocke la liste des positions de tuiles sur la face du cube Rubik.
           #enumerate est une fonction de Python qui permet d'itérer sur une liste en fournissant à
           #la fois l'élément actuel et son indice.
            for vec in side:
                carré = box(pos=vec,size=vector(0.98,0.98,0.1),color=colors[rank])
            
               #box sert à créer la forme des petits carrés
               #position des carrés
               #size:largeur=0.98 longueur=0.98 et profondeur=0.1
               #color=colors[rank] car au début on a définie les couleurs des faces (front=rouge)
                carré.rotate(angle = angle[rank][0],axis=angle[rank][1])
                
                #on fait la rotation de chaque face d'un angle autour d'un axe
                #pour creer le premier rubiks cube
               
                self.carrés.append(carré)
                # on stock  la pos et la couleur de chaque petit carré
        
        #positions
        #on va créer un dictionnaire
        #Les listes vides seront utilisées pour stocker les coordonnées des petits carrés sur
        #chaque face.
    
        self.positions = {'top':[],'left':[],'back':[],'front':[],'right':[],'bottom':[]}
        #variables
        self.rotate = [None,0,0]
        #None: on n'a pas fait de rotation
        #on va créer une liste vide qui sera utilisée pour stocker une séquence de mouvements
        #effectués sur le Rubiks cube

        self.mouvements = []
        
    def liste_des_couleurs(self): #pour récuperer les couleurs des petits carré après avoir effectué un mouvement
        print(dc.decode_position(self.carrés))
        return dc.decode_position(self.carrés)
    
    def reset_positions(self):
        self.positions = {'top':[],'left':[],'back':[],'front':[],'right':[],'bottom':[]}
        #Boucle pour mettre à jour les positions

        for carré in self.carrés:
            if carré.pos.z > 0.4:#Si la position z de du carré est supérieure à 0.4,
            #cela signifie que le carré appartient à la face avant ('front').
            # et pour appliquer la rotation sur toute la face 

                self.positions['front'].append(carré)
            if carré.pos.x > 0.4:
                self.positions['right'].append(carré)
            if carré.pos.z < -0.4:
                self.positions['back'].append(carré)
            if carré.pos.x < -0.4:
                self.positions['left'].append(carré)
            if carré.pos.y > 0.4:
                self.positions['top'].append(carré)
            if carré.pos.y < -0.4:
                self.positions['bottom'].append(carré)
        for key in self.positions.keys():#key représente les différentes faces
            self.positions[key] = set(self.positions[key])#set() qui prend une
            #liste en argument et crée un ensemble contenant 
            #les éléments uniques de cette liste pour garentir que chaque pos est unique
            #car on est en 3D
    

    def animations(self):
        
        if self.rotate[0] == 'back_counterclockwise' :
            # Lorsque cliqué sur 'back_counterclockwise'
            pieces = self.positions['back']  # Récupérer la liste des carrés de la face arrière
            for carré in pieces:  # Itérer sur chaque carré de la face arrière et appliquer
            # une rotation dans le sens anti-horaire autour de l'axe z [vector(0,0,-1)] avec un angle
            # défini par self.dA.

                carré.rotate(angle=(self.dAngle), axis=vector(0,0,-1), origin=vector(0,0,0))
            # La rotation est effectuée autour de l'origine

            self.rotate[1] += self.dAngle
        # Après avoir tourné chaque carré, l'angle de rotation total (self.rotate[1]) est mis à jour en ajoutant la valeur
        # de self.dAngle. Cela permet de suivre les rotations totales effectuées.
    
        elif self.rotate[0] == 'left_counterclockwise' :
            pieces = self.positions['left']
            for carré in pieces:
                carré.rotate(angle=(self.dAngle),axis = vector(-1,0,0),origin=vector(0,0,0))
            self.rotate[1] += self.dAngle
        
        elif self.rotate[0] == 'bottom_counterclockwise' :#rotation autour de y
            pieces = self.positions['bottom']
            for carré in pieces:
                carré.rotate(angle=(self.dAngle),axis = vector(0,-1,0),origin=vector(0,0,0))
            self.rotate[1] += self.dAngle
        
        
        elif self.rotate[0] == 'back_clockwise' :
            pieces = self.positions['back']
            for carré in pieces:
                carré.rotate(angle=(-self.dAngle),axis = vector(0,0,-1),origin=vector(0,0,0))
            self.rotate[1] += self.dAngle
        elif self.rotate[0] == 'left_clockwise' :
            pieces = self.positions['left']
            for carré in pieces:
                carré.rotate(angle=(-self.dAngle),axis = vector(-1,0,0),origin=vector(0,0,0))
            self.rotate[1] += self.dAngle
        
        elif self.rotate[0] == 'bottom_clockwise' :
            pieces = self.positions['bottom']
            for carré in pieces:
                carré.rotate(angle=(-self.dAngle),axis = vector(0,-1,0),origin=vector(0,0,0))
            self.rotate[1] += self.dAngle
            
        if self.rotate[1] + self.dAngle/2 > self.rotate[2] and \
            self.rotate[1] - self.dAngle/2 < self.rotate[2]:  #le but c'est de se rapprocher le maximum de l'angle de rotation
                                                              #voulu =pi/2
            self.rotate = [None,0,0]
            self.reset_positions()
    
    
    def rotate_back_counterclockwise(self):
        if self.rotate[0] == None:
            self.rotate = ['back_counterclockwise',0,np.pi/2]
    def rotate_left_counterclockwise(self):
        if self.rotate[0] == None:
            self.rotate = ['left_counterclockwise',0,np.pi/2]
    
    def rotate_bottom_counterclockwise(self):
        if self.rotate[0] == None:
            self.rotate = ['bottom_counterclockwise',0,np.pi/2]
    
    def rotate_back_clockwise(self):
        if self.rotate[0] == None:
            self.rotate = ['back_clockwise',0,np.pi/2]
    def rotate_left_clockwise(self):
        if self.rotate[0] == None:
            self.rotate = ['left_clockwise',0,np.pi/2]
    
    def rotate_bottom_clockwise(self):
        if self.rotate[0] == None:
            self.rotate = ['bottom_clockwise',0,np.pi/2]
    
    

        
   
            
    def mouvement(self): # qd on clique sur random mvt ou solve it
        possible_mouvements = ["B","L","D","B'","L'","D'"]        
        if self.rotate[0] == None and len(self.mouvements) > 0:
            if self.mouvements[0] == possible_mouvements[0]:
                self.rotate_back_clockwise()
            elif self.mouvements[0] == possible_mouvements[1]:
                self.rotate_left_clockwise()
            elif self.mouvements[0] == possible_mouvements[2]:
                self.rotate_bottom_clockwise()
            elif self.mouvements[0] == possible_mouvements[3]:
                self.rotate_back_counterclockwise()
            elif self.mouvements[0] == possible_mouvements[4]:
                self.rotate_left_counterclockwise()
            elif self.mouvements[0] == possible_mouvements[5]:
                self.rotate_bottom_counterclockwise()

            self.mouvements.pop(0)
            
    def scramble(self): # pour faire des mouvements aléatoires
         possible_mouvements = ["B","L","D","B'","L'","D'"]
         for i in range(4):
             x = random.choice(possible_mouvements)
             self.mouvements.append(x)
             
    
    def clear_label(self):
    # Remove the text label
        self.instruction.text = ""
    
        
    def chiffres_to_lettres(self):
        A=[[0, 0, 4, 3],   # la liste des couleurs récupérer du code de clément (le choix de l'utilisateur)
           [1, 3, 5, 2],
           [3, 2, 0, 4],
           [3, 2, 2, 5],
           [1, 0, 4, 4],
           [5, 1, 1, 5]]
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    A[i][j] = vector(1, 1, 1) # white
                elif A[i][j] == 1:
                    A[i][j] = vector(0, 1, 0) # green
                elif A[i][j] == 2:
                    A[i][j] = vector(1, 0, 1) # purple
                elif A[i][j] == 3:
                    A[i][j] = vector(1, 0, 0) # red
                elif A[i][j] == 4:
                    A[i][j] = vector(0, 0, 1) # blue
                elif A[i][j] == 5:
                    A[i][j] = vector(1, 1, 0) # yellow
        return A
    
    
    
    
    def choose_colors(self):
        self.changer_button_next_step()
        couleurs = self.chiffres_to_lettres()
        self.en_marche = True
        for carré in self.carrés:
            carré.visible = False # pour cacher l'ancien cube déja crée
        self.carrés = []
        self.dAngle = np.pi/40 
        self.values = []
        self.instruction = label(text="", pos=vector(0, 1.25, 1))
     
        sphere(pos=vector(0,0,0),size=vector(1,1,1),color=vector(0,0,0))

        carré_pos = [[vector(0.5,1, -0.5), vector(0.5, 1, 0.5),          # top
                     vector(-0.5, 1, 0.5), vector(-0.5, 1, -0.5),
                     ],
                     [vector(-1, 0.5, -0.5), vector(-1, 0.5,0.5),          # left
                      vector(-1,-0.5, 0.5),vector(-1, -0.5, -0.5),
                      ],
                     [vector(0.5, -0.5, -1), vector(0.5, 0.5, -1),        # back
                      vector(-0.5, 0.5, -1), vector(-0.5, -0.5, -1),
                      ], 
                     [vector(0.5, 0.5, 1),vector(0.5, -0.5, 1),           #front
                     vector(-0.5, -0.5, 1),vector(-0.5,0.5 , 1),
                     ],
                    [vector(1, -0.5, -0.5),vector(1, -0.5, 0.5),         # right
                     vector(1, 0.5, 0.5),vector(1, 0.5, -0.5),
                     ],
                    [vector(-0.5, -1, -0.5),vector(-0.5, -1, 0.5),     # bottom
                    vector(0.5, -1, 0.5),vector(0.5, -1, -0.5), 
                     ],
                   ]
        self.carrés=[]
        angle = [(np.pi/2,vector(1,0,0)), (np.pi/2,vector(0,1,0)), (0,vector(0,0,0)), (0,vector(0,0,0)), (np.pi/2,vector(0,1,0)), (np.pi/2,vector(1,0,0))]
        
        for rank,side in enumerate(carré_pos):
            for i in range(len(side)):
                carré = box(pos=side[i],size=vector(0.98,0.98,0.1),color=couleurs[rank][i])
                carré.rotate(angle = angle[rank][0],axis=angle[rank][1])
                self.carrés.append(carré)
       
        self.positions = {'top':[],'left':[],'back':[],'front':[],'right':[],'bottom':[]}
        self.rotate = [None,0,0]
        self.mouvements = []
        
        
    
    def changer_button_next_step(self):
        self.bouton.text = "solve it!"
        
        
    def changer_bouton_solve(self):
        self.bouton.text = 'next_step'
        
        
    def control(self):
        button(bind=self.rotate_back_clockwise, text='B')
        button(bind=self.rotate_back_counterclockwise, text="B'")
        button(bind=self.rotate_left_clockwise, text='L')
        button(bind=self.rotate_left_counterclockwise, text="L'") 
        button(bind=self.rotate_bottom_clockwise, text='D')
        button(bind=self.rotate_bottom_counterclockwise, text="D'")
        button(bind=self.scramble, text='random_mouvement')
        self.bouton=button(bind=self.solve, text='solve it!')
        button(bind=self.liste_des_couleurs, text='liste des couleurs')
        button(bind=self.choose_colors, text='choisir son rubiks cube')
            
        
    def solve(self):
        # print(self.liste_des_couleurs())
        # print(bsf.solved_pos)
        # print(bsf.bidirectional_solve(self.liste_des_couleurs(), bsf.solved_pos, 6))
        values = bsf.fcte_to_lettres(bsf.bidirectional_solve(self.liste_des_couleurs(), bsf.solved_pos, 6))
        
        if not values:
            self.instruction.text = "Cube résolu"
            self.changer_button_next_step()
            sleep(2)
            self.clear_label()
            return
        else:
            self.mouvements.append(values[0])
            self.mouvement() 
            self.changer_bouton_solve()
        if len(values) == 1:
            self.instruction.text = "Cube résolu"
            self.changer_button_next_step()
            sleep(2)
            self.clear_label()
            return
        
        
    def update(self):
        rate(65)
        self.animations() 
        self.mouvement()
        
        
    def start(self):
        self.reset_positions()
        self.control()
        while self.en_marche:
            rate(65)
            self.animations() 
            self.mouvement()
