from vpython import *
import numpy as np

print("1. Imports basiques OK")

class Rubic_Cube():
    def __init__(self):
        print("2. Initialisation commence...")
        self.scene = canvas(width=1200, height=800)
        print("3. Scene créée")
        
        self.en_marche = True
        self.carrés = [] 
        print("4. Variables de base OK")
        
        sphere(pos=vector(0,0,0), size=vector(1,1,1), color=vector(0,0,0))
        print("5. Sphère créée")
        
        self.instruction = label(text="Test", pos=vector(0, 1.25, 1))
        print("6. Label créé")
        
    def start(self):
        print("7. Start lancé")
        self.instruction.text = "Cube OK!"

print("Test commence...")
cube = Rubic_Cube()
print("8. Cube créé avec succès")
cube.start()
print("9. Done")