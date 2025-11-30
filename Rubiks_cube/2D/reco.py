import cv2

"""
Ordre des faces:
On commence par la face avec le Blanc du coin Bleu-Blanc-Rouge en bas à droite 
On tourne vers la gauche pour montrer la face de droite 
On répète cette rotation vers la gauche encore 3 fois pour retomber sur la face initiale
On montre la face du bas (avec le Rouge du coin Bleu-Blanc-Rouge)
On tourne 2 fois vers le haut pour montrer la face du haut 
"""

def color_detect(h, s, v):
    """
    Parameters
    ----------
    h = int
    h correspond à la teinte
    s = int
    s correspond à la saturation (à quelle point c'est coloré)
    v= int
    v correspond à la valeur (= la légèreté)
    ________
    on définie les couleurs qui nous interessent
    """
    if h < 5 and s>5 or h>170:
        return 'red'
    elif 130 <= h < 180:
        return 'purple'
    elif 20 < h <= 25:
        return 'yellow'
    elif 70 <= h <= 85 and s > 100 and v < 180:
        return 'green'
    elif h <= 130 and s > 85:
        return 'blue'
    elif h <= 100 and s < 10 and v < 200:
        return 'white'
    return 'white'

def ajouter_couleurs(frame, stickers): 
    """
    Parameters
    ----------
    frame : numpy.ndarray
    frame correspond à la lecture de la video
    stickers = list
    les stickers correspondent aux cases dans lesquelles on place le Rubik's Cube où les couleurs sont détectées
    ________
    on enregistre les couleurs qui se trouvent dans les cases
    """
    detected_colors = []
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    for x, y in stickers: # on detecte les couleurs dans les 4 cases
        h, s, v = hsv_frame[y, x]
        color = color_detect(h, s, v)
        detected_colors.append(color)
    return detected_colors, frame

def definir_case(frame,stickers,compteur) : 
    """
    Parameters
    ----------
    frame : numpy.ndarray
    frame correspond à la lecture de la video
    stickers = list
    les stickers correspondent aux cases dans lesquelles on place le Rubik's Cube
    compteur = int
    on compte le nombre de faces 
    ________
    on définit les 4 cases
    """
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    for x, y in stickers:
        h, s, v = hsv_frame[y, x]
        color = color_detect(h, s, v)
        cv2.rectangle(frame, (x-20, y-20), (x+20, y+20), (255, 255, 255), 2) 
        cv2.putText(frame, color, (x-10, y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
    # Fixer les trois cases au départ : blanc, rouge, bleu 
    if compteur == 1:
        cv2.rectangle(frame, (200-20, 200-20), (200+20, 200+20), (255, 255, 255), -1)
    elif compteur == 4:
        cv2.rectangle(frame, (100-20, 200-20), (100+20, 200+20), (255, 0, 0), -1)
    elif compteur == 5:
        cv2.rectangle(frame, (200-20, 100-20), (200+20, 100+20), (0, 0, 255), -1)
    
        
    
def main():
    stickers = [ # on défini l'emplacement des 4 cases
        [200,100],[200, 200],
        [100,200],[100, 100]
    ]
    compteur = 1

    instructions = ('Montrer la face avec le blanc du coin Bleu-Blanc-Rouge en bas a droite',
                    'Tourner dans le sens anti horaire',
                    'Tourner dans le sens anti horaire',
                    'Tourner dans le sens anti horaire',
                    'Tourner dans le sens anti horaire et montrer la face du bas (facette Rouge en haut a droite)',
                    'Tourner 2 fois vers le haut pour montrer la face du haut')

    cap = cv2.VideoCapture(0) #on ouvre la caméra de l'ordinateur
    config = []
    while True:
        ret, frame = cap.read() 
        if not ret:
            break
        definir_case(frame,stickers,compteur) 
        if cv2.waitKey(1) & compteur == 7: # si les 6 faces ont été montré, on ferme la fenêtre
            break
        a = f"face {compteur}" #on indique à l'utilisateur à quelle face du Rubik's Cube il en est
        
        cv2.putText(frame, a, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,25,235),2,cv2.LINE_4)
        cv2.putText(frame, instructions[compteur-1], (50,300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,25,235),2,cv2.LINE_4)
        cv2.putText(frame, 'Et cliquer sur C', (50,350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,25,235),2,cv2.LINE_4)
        if cv2.waitKey(1)==ord('c') : # il faut cliquer sur 'c' pour enregistrer les couleurs 
            detected_colors, frame = ajouter_couleurs(frame, stickers)
            config.append(detected_colors)
            compteur += 1
        cv2.imshow('Frame', frame)

    cap.release()
    cv2.destroyAllWindows()
    config = [config[0], config[1], config[5], config[4], config[3], config[2]]
    return config    
    
    
    
    
    
    
    