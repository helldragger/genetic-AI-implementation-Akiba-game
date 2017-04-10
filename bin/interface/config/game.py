"""
The playing mode configuration panel
"""

import tkinter as tk


class GameSettings(tk.LabelFrame):
    def __init__(self, master):
        """
        Initialize the config panel and displays it with the main menu as a master window
        :param master: the main menu
        """
        super(GameSettings, self).__init__(master, text="Game settings")
        self.master = master
        self.result = ''
        self.ia_or_not = tk.BooleanVar()
        self.but__ia_or_not = tk.Checkbutton(master,
                                             text="Against IA",
                                             variable=self.ia_or_not,
                                             onvalue=True,
                                             offvalue=False,
                                             command=self.update_diff_choice)
        self.but__ia_or_not.pack(anchor=tk.W)
        self.ia_difficulty = tk.IntVar()
        self.ia_genome = ''
        self.really_easy_ia_difficulty = tk.Radiobutton(master, text="Casual", variable=self.ia_difficulty, value=0,
                                            command=self.update_gen_choice, state='disabled')

        self.easy_ia_difficulty = tk.Radiobutton(master, text="Easy", variable=self.ia_difficulty, value=1,
                                            command=self.update_gen_choice, state='disabled')

        self.average_ia_difficulty = tk.Radiobutton(master, text="Average", variable=self.ia_difficulty, value=2,
                                            command=self.update_gen_choice, state='disabled')

        self.harder_ia_difficulty = tk.Radiobutton(master, text="Rock Hard", variable=self.ia_difficulty, value=3,
                                            command=self.update_gen_choice, state='disabled')

        self.damned_ia_difficulty = tk.Radiobutton(master, text="You're doomed", variable=self.ia_difficulty, value=4,
                                            command=self.update_gen_choice, state='disabled')

        self.really_easy_ia_difficulty.pack(anchor=tk.E)
        self.easy_ia_difficulty.pack(anchor=tk.E)
        self.average_ia_difficulty.pack(anchor=tk.E)
        self.harder_ia_difficulty.pack(anchor=tk.E)
        self.damned_ia_difficulty.pack(anchor=tk.E)
        self.but__validate = tk.Button(master,
                                       text='Start the game',
                                       command=self.set_result)
        self.but__validate.pack(anchor=tk.S)
        self.master.mainloop()

    def update_gen_choice(self):
        """
        Updates the selected IA genome based on the difficulty choosed
        """
        if self.ia_difficulty.get() == 0:
            self.ia_genome = '000000000000000000000000000000000000000000000000000000000000'
        elif self.ia_difficulty.get() == 1:
            self.ia_genome = '110011000110100101000010110010101100001011010011011111110000'
        elif self.ia_difficulty.get() == 2:
            self.ia_genome = '111010011111101010110011010111010000000110101101100100100001'
        elif self.ia_difficulty.get() == 3:
            self.ia_genome = '111010011111101010110011010111010000000110101101100100100001'
        else:
            self.ia_genome = '100110010001110000010100000001100011010011100001000001101000'

    def update_diff_choice(self):
        """
        Dis/enable the difficulty choice when the IA mode is toggled Off/On respectively
        """
        if self.ia_or_not.get():
            self.really_easy_ia_difficulty.config(state='normal')
            self.easy_ia_difficulty.config(state='normal')
            self.average_ia_difficulty.config(state='normal')
            self.harder_ia_difficulty.config(state='normal')
            self.damned_ia_difficulty.config(state='normal')
        else:
            self.really_easy_ia_difficulty.config(state='disabled')
            self.easy_ia_difficulty.config(state='disabled')
            self.average_ia_difficulty.config(state='disabled')
            self.harder_ia_difficulty.config(state='disabled')
            self.damned_ia_difficulty.config(state='disabled')

    def set_result(self):
        """
        Sets the final configuration into the args format used by the main program
        """
        self.result = (self.ia_or_not, self.ia_genome if self.ia_or_not else '')
        self.master.destroy()
