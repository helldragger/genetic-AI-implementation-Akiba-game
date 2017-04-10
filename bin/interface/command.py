import tkinter as tk
from tkinter import messagebox


def halp():
    """
    Shows a pop up containing the rules of the game
    """
    rules = "Le but du jeu est d'éliminer 6 boules rouges en premier ou de décimer l'intégralité des boules du joueur adverse en respectant des regles de déplacement précises: Pour pousser une de ses boules dans une direction, le joueur doit avoir une case de libre derriere la boule pour pouvoir poser son doigt. Un joueur ne peux pas essayer de faire la mouvement inverse du dernier coup de son  adversaire, pour ne pas bloquer indéfiniment le jeu. Un joueur ne peux pas faire tomber une de ses boules du plateau volontairement."
    tk.Toplevel()
    messagebox.showinfo("Regles du jeu", rules)


class CommandUI(tk.LabelFrame):
    """
    Shows the command frame
    """

    def __init__(self, master, root):
        tk.LabelFrame.__init__(self, master, text='MENU', width=700)
        self.new_game_button = tk.Button(self, text='New game', command=root.new_game)
        self.halp_button = tk.Button(self, text='Rules', command=halp)

        self.halp_button.grid(column=1, row=0)
        self.new_game_button.grid(column=0, row=0)
