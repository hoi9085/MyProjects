import tkinter as tk
import random
import codebreaker2 as cb2
import common

class Mastermind:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Mastermind")
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'brown', 'black', 'white']
        self.pattern = [random.choice(self.colors) for _ in range(4)]  # Combinaison par défaut
        self.attempts = 0
        self.chosen_colors = []
        self.color_row = []
        self.color_series = [[]]
        self.starting_color_buttons = []
        self.create_widgets()
        self.bien_places = 0
        self.mal_places = 0
        
    def create_widgets(self):
        self.canvas = tk.Canvas(self.parent, width=600, height=700)
        self.canvas.grid(row=5, column=10, columnspan=20)
        
        self.color_buttons = []
        for i, color in enumerate(self.colors):
            button = tk.Button(self.parent, bg=color, width=2, command=lambda c=color: self.select_color(c))
            button.grid(row=1, column=i)
            self.color_buttons.append(button)
        
        self.submit_button = tk.Button(self.parent, text="Soumettre", command=self.submit_guess)
        self.submit_button.grid(row=1, column=23)

        
        self.guess_display = tk.Label(self.parent, text="Choisissez une couleur pour chaque emplacement", font=("Helvetica", 10))
        self.guess_display.grid(row=5, column=10, columnspan=6)
        self.reset_button = tk.Button(self.parent, text="Réinitialiser", command=self.reset_game)
        self.reset_button.grid(row=7, column=23, columnspan=6)
        self.play_a_human_button = tk.Button(self.parent, text="play against a human", command=self.play_a_human)
        self.play_a_human_button.grid(row=6, column=0, columnspan=6)
        self.clear_button = tk.Button(self.parent, text="Effacer la ligne", command=self.clear_row)
        self.clear_button.grid(row=7, column=36)  # Ajouter le bouton Effacer la ligne ici
        
    def play_a_human(self):
        self.starting_color_buttons = []
        for i, color in enumerate(self.colors):
            button = tk.Button(self.parent, bg=color, width=2, command=lambda c=color: self.set_starting_color(c))
            button.grid(row=7, column=i)
            self.starting_color_buttons.append(button)
        
        
      
    def clear_row(self):
    # Vérifier si la supposition n'a pas encore été soumise
        if len(self.chosen_colors) == 0:
            return
    
    # Supprimer les cercles un par un
        for _ in range(min(4, len(self.chosen_colors))):
            item = self.color_row.pop()
            self.canvas.delete(item)
            self.chosen_colors.pop()

    # Réinitialiser le texte d'affichage pour le choix des couleurs
        self.guess_display.config(text="Choisissez une couleur pour chaque emplacement")
        
    def select_color(self, color):
    # Vérifier si le nombre de couleurs choisies est inférieur à 4 ou si le nombre d'exactitudes est différent de 4
        if len(self.chosen_colors) != 4 and self.bien_places != 4:
            # Ajouter la couleur sélectionnée à la liste des couleurs choisies
            self.chosen_colors.append(color)
    
            # Dessiner les nouvelles couleurs dans la rangée
            x = 300 + (len(self.chosen_colors) - 1) * 50
            y = 50 + len(self.color_series) * 50  # Ajuster la position verticale
            oval_id = self.canvas.create_oval(x, y, x + 40, y + 40, fill=color)
        
            # Ajouter l'ID de l'ovale à la liste color_row
            self.color_row.append(oval_id)
        
        if len(self.chosen_colors) == 4:
            # Afficher un message si le nombre de couleurs choisies est déjà 4
            self.guess_display.config(text="vous avez déjà choisi 4 couleurs")
        

            
    def submit_guess(self):
        self.guess_display.config(text="")
        if len(self.chosen_colors) < 4:
        # Afficher un message si moins de 4 couleurs ont été choisies
            self.guess_display.config(text="Il faut choisir exactement 4 couleurs avant de soumettre")
        if len(self.chosen_colors) == 4:
                self.attempts += 1
                guess = self.chosen_colors.copy()
                feedback = self.check_guess(guess)
                self.update_feedback(feedback)
                self.bien_places, _ = feedback
                if self.bien_places != 4 and len(self.chosen_colors)==4:
            # Stocker la série actuelle dans la liste des séries
                    self.color_series.append(self.chosen_colors)
            
            # Effacer les couleurs choisies pour permettre une nouvelle série
                    self.chosen_colors = []
                if self.attempts < 10 and self.bien_places!=4:
                    self.guess_display.config(text="Choisissez une couleur pour chaque emplacement")
        
            
    def check_guess(self, guess): # la fonction evaluation
        self.bien_places, self.mal_places = 0, 0
        combinaison1, combinaison2 = [], []
        
        if len(guess) != 4:
            return (0, 0) # Renvoyer (0, 0) si la supposition n'est pas valide

        for i in range(len(guess)):
            if guess[i] == self.pattern[i]:
                self.bien_places += 1
            else:
                combinaison1.append(self.pattern[i])
                combinaison2.append(guess[i])

        for e in combinaison2:
            if e in combinaison1:
                self.mal_places += 1
                combinaison1.remove(e)
        if (self.bien_places==0 and self.mal_places == 0) or guess==[]:
            return (0, 0)
        return self.bien_places, self.mal_places


    def update_feedback(self, feedback):
        self.bien_places, self.mal_places = feedback
        if self.bien_places == 4:
            self.guess_feedback = tk.Label(self.parent, text="Félicitations ! \nVous avez trouvé \nla combinaison en \n{} tentatives.".format(self.attempts), font=("Helvetica", 10))
            self.guess_feedback.grid(row=1, column=20, columnspan=6)
            self.guess_display.config(text="")
            self.play_a_human_button.config(text="")
            self.another_game_button=tk.Button(self.parent, text="jouer une autre partie", command=self.reset_game)
            self.another_game_button.grid(row=5, column=10, columnspan=6)
            for button in self.color_buttons:
                button.config(state="disabled")
            self.submit_button.grid_remove()
            if hasattr(self, "starting_color_buttons"):
                for button in self.starting_color_buttons:
                    button.destroy()
            for i in range(self.bien_places):
                x = 500 + i * 30
                y = 55 + len(self.color_series) * 50
                self.canvas.create_oval(x, y, x+12, y +12, fill="white")
            
        else:
            
            if self.attempts >= 10:
                self.another_game_button=tk.Button(self.parent, text="jouer une autre partie", command=self.reset_game)
                self.another_game_button.grid(row=5, column=10, columnspan=6)
                self.guess_feedback = tk.Label(self.parent, text="Vous avez atteint le \nnombre maximal de tentatives. \nLa combinaison était \n{}".format(self.pattern), font=("Helvetica", 10))
                self.guess_feedback.grid(row=1, column=20, columnspan=6)
                self.guess_display.config(text="")
                self.play_a_human_button.config(text="")
                for button in self.color_buttons:
                    button.config(state="disabled")
                self.submit_button.grid_remove()
                if hasattr(self, "starting_color_buttons"):
                    for button in self.starting_color_buttons:
                        button.destroy()
                for i in range(self.bien_places):
                    x = 500 + i * 30
                    y = 55 + len(self.color_series) * 50
                    self.canvas.create_oval(x, y, x+12, y +12, fill="white")
            
            # Affichage des cercles noirs pour les couleurs présentes mais mal placées
                for i in range(self.mal_places):
                    x = 500 +i* 30
                    y = 70 + len(self.color_series) * 50
                    self.canvas.create_oval(x, y, x + 12, y + 12, fill="black")
        
                
            else:
                for i in range(self.bien_places):
                    x = 500 + i * 30
                    y = 55 + len(self.color_series) * 50
                    self.canvas.create_oval(x, y, x+12, y +12, fill="white")
            
            # Affichage des cercles noirs pour les couleurs présentes mais mal placées
                for i in range(self.mal_places):
                    x = 500 +i* 30
                    y = 70 + len(self.color_series) * 50
                    self.canvas.create_oval(x, y, x + 12, y + 12, fill="black")
        
                
    def set_starting_color(self, color):
        # Mettre à jour la combinaison de départ
        self.pattern.append(color)
        self.pattern = self.pattern[-4:]  # Limiter la combinaison à 4 couleurs
        
        


    def reset_game(self):
    # Réinitialiser toutes les variables
        self.attempts = 0
        self.chosen_colors = []
        self.color_row = []
        self.color_series = [[]]
        self.bien_places = 0
        self.mal_places = 0
        self.pattern = [random.choice(self.colors) for _ in range(4)]  # Générer une nouvelle combinaison par défaut

    # Réinitialiser l'affichage
        self.canvas.delete("all")  # Effacer tous les éléments du canvas
        self.guess_display.config(text="Choisissez une couleur pour chaque emplacement")
        
    # Rétablir les boutons de couleur
        for button in self.color_buttons:
            button.config(state="normal")

    # Rétablir les boutons "Soumettre" et "play against a human"
        self.submit_button.grid(row=1, column=23)
        self.play_a_human_button.grid(row=6, column=0, columnspan=6)
        self.reset_button.grid(row=7, column=23, columnspan=6)

    # Détruire les boutons de couleur de départ
        for button in self.starting_color_buttons:
            button.destroy()

    # Supprimer l'affichage du feedback s'il existe
        if hasattr(self, "guess_feedback"):
            self.guess_feedback.destroy()

    # Supprimer le bouton "Jouer une autre partie" s'il existe
        if hasattr(self, "another_game_button"):
            self.another_game_button.destroy()

        self.play_a_human_button.config(text="play against a human")


root = tk.Tk()
game = Mastermind(root)
root.mainloop()