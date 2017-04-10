"""
The main configuration manager
"""
import tkinter as tk
import bin.interface.config.game as gamesettings
import bin.interface.config.training as trainingsettings


class Config:
    def __init__(self, mode):
        """
        Initialize the config window and opens the corresponding panel based on the mode choosed by the user before
        getting the args passed by the corresponding panel

        :param mode: the mode the user choosed
        """
        self.w = tk.Tk()
        self.args = ()

        if mode == 'training':
            self.args = trainingsettings.TrainingSettings(self.w).result
        else:
            self.args = gamesettings.GameSettings(self.w).result
