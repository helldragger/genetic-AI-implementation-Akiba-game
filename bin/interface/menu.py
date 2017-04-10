"""
Launcher GUI, makes the link between every mode of the project
"""

import tkinter as tk
import bin.interface.config.config as config


class MainMenu:
    def __init__(self):
        """
        Initialize the main menu
        """
        self.mode = ''
        self.args = ()
        self.start_menu = tk.Tk()
        self.zone = tk.Frame(self.start_menu)
        self.gui_button = tk.Button(self.zone, text="GUI mode", command=self.gui)
        self.trn_button = tk.Button(self.zone, text="AI training mode", command=self.training)
        self.cmd_button = tk.Button(self.zone, text="Command-line mode", command=self.cmd)
        self.gui_button.pack()
        self.cmd_button.pack()
        self.trn_button.pack()
        self.zone.pack()
        self.start_menu.mainloop()

    def set_args(self):
        """
        Get the args passed through the mode specific config panels
        """
        self.start_menu.destroy()
        self.args = config.Config(self.mode).args

    def gui(self):
        """
        Determines the mode the user choose as GUI mode and launch the corresponding arg
        """
        self.mode = 'gui'
        self.set_args()

    def training(self):
        """
        Determines the mode the user choose as AI training mode and launch the corresponding arg
        """
        self.mode = 'training'
        self.set_args()

    def cmd(self):
        """
        Determines the mode the user choose as command line mode and launch the corresponding arg
        """
        self.mode = 'commandline'
        self.set_args()



