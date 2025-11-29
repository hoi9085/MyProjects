import CUBE
import  Bidirectional_solve_fonctionnel
import numpy as np


def color_detect(color_value):
    # Extraction des composantes (x, y, z) de color_value
    value = (color_value.x, color_value.y, color_value.z)
    
    # Initialisation de la variable de résultat de couleur
    color_result = None
    
    # Vérification de la couleur en fonction des valeurs de composantes
    if value == (1, 0, 0):  # Si les composantes correspondent au rouge
        color_result = 'R'  # Attribuer 'R' pour rouge
        
    elif value == (1, 1, 0):  
        color_result = 'Y'  # jaune
        
    elif value == (1, 0, 1 ):  
        color_result = 'P'  # move
        
    elif value == (1, 1, 1):  
        color_result = 'W'  # blanc
        
    elif value == (0, 0, 1):  
        color_result = 'B'  # bleu
        
    elif value == (0, 1, 0):  
        color_result = 'G'  # vert
    
    # Retourner le résultat de la détection de couleur
    return color_result




def verifier_pos_carré(pos, bounds):
    # Extraction des coordonnées x, y, z de la position (pos)
    x, y, z = pos
    
    # Extraction des bornes (x_bound, y_bound, z_bound)
    x_bound, y_bound, z_bound = bounds
    
    # Vérification si les coordonnées de pos sont proches des bornes dans une marge de ±0.2
    # et retourne True si oui, False sinon
    return (-0.2 <= x - x_bound <= 0.2) and (-0.2 <= y - y_bound <= 0.2) and (-0.2 <= z - z_bound <= 0.2)



def decode_position(cube):
#parcourt les carrés du Rubik's Cube et détermine la couleur de chaque carré en fonction
#de sa position. Elle construit une liste de longueur 24, où chaque élément représente la couleur d'un petit carré
#sur le cube, en fonction de sa position. Cette liste est ensuite retournée. ces couleurs sont mises dans la liste
#le meme ordre définit par  carré_pos
    
    value = np.zeros((6, 4), dtype = object)  # Un Rubik's Cube 2x2 a 24 carrés
    for carré in cube:
        pos = (carré.pos.x, carré.pos.y, carré.pos.z)
        #print(verifier_pos_carré(pos, (-0.5, 0.5, 1)))
        if verifier_pos_carré(pos, (-0.5, 0.5, 1)):  # Front
            value[3][3] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (0.5, 0.5, 1)):
            value[3][0] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-0.5, -0.5, 1)):
            value[3][2] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (0.5, -0.5, 1)):
            value[3][1] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (1, 0.5, 0.5)):  # Right
            value[4][2] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (1, 0.5, -0.5)):
            value[4][3] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (1, -0.5, 0.5)):
            value[4][1] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (1, -0.5, -0.5)):
            value[4][0] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-0.5, 0.5, -1)):  # Back
            value[2][2] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (0.5, 0.5, -1)):
            value[2][1] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-0.5, -0.5, -1)):
            value[2][3] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (0.5, -0.5, -1)):
            value[2][0] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-1, 0.5, 0.5)):  # Left
            value[1][1] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-1, 0.5, -0.5)):
            value[1][0] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-1, -0.5, 0.5)):
            value[1][2] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-1, -0.5, -0.5)):
            value[1][3] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-0.5, 1, -0.5)):  # top
            value[0][3] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (0.5, 1, -0.5)):
            value[0][0] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-0.5, 1, 0.5)):
            value[0][2] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (0.5, 1, 0.5)):
            value[0][1] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-0.5, -1, -0.5)):  # bottom
            value[5][0] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (0.5, -1, -0.5)):
            value[5][3] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (-0.5, -1, 0.5)):
            value[5][1] = color_detect(carré.color)
        elif verifier_pos_carré(pos, (0.5, -1, 0.5)):
            value[5][2] = color_detect(carré.color)
    #Convertir les éléments de la matrice en chaînes de caractères et les concaténer avec des virgules.
    str_value = np.array([[str(item) for item in row] for row in value])
    return str_value


