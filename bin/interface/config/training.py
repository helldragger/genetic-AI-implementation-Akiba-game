"""
The AI training mode config panel
"""

import tkinter as tk
import bin.AI.genetics as gn


class TrainingSettings(tk.LabelFrame):
    def __init__(self, master):
        """
        Initialize the config panel and displays it with the main menu as a master window
        :param master: the main menu
        """
        super(TrainingSettings, self).__init__(master, text="Training settings")
        self.master = master
        self.result = ''

        self.session_frame = tk.LabelFrame(master,
                                           text='Training session settings')
        self.max_pop_label = tk.Label(self.session_frame,
                                      text='Max population :')
        self.max_pop_data = tk.Scale(self.session_frame,
                                      from_=5,
                                      to=20,
                                      orient=tk.HORIZONTAL)

        self.nb_iter_label = tk.Label(self.session_frame,
                                      text='Number of iterations (0 = infinite) :')
        self.nb_iter_data = tk.Scale(self.session_frame,
                                     from_=0,
                                     to=100,
                                     orient=tk.HORIZONTAL)

        self.do_graphs = tk.BooleanVar()
        self.graphs_label = tk.Label(self.session_frame, text='Display some stats on the fly?')
        self.graphs_data = tk.Checkbutton(self.session_frame, variable=self.do_graphs, onvalue=True, offvalue=False)

        self.do_verbose = tk.BooleanVar()
        self.verbose_label = tk.Label(self.session_frame, text='Display progression?')
        self.verbose_data = tk.Checkbutton(self.session_frame, variable=self.do_verbose, onvalue=True, offvalue=False)

        self.custom_frame = tk.LabelFrame(master, text='Custom first parents')
        self.warning = tk.Label(self.custom_frame, text="WARNING! USE AT YOUR OWN RISKS!")

        self.p1_string = tk.StringVar()
        self.p1_label = tk.Label(self.custom_frame, text="First parent genome string:")
        self.p1_data = tk.Entry(self.custom_frame, textvariable=self.p1_string)

        self.p2_string = tk.StringVar()
        self.p2_label = tk.Label(self.custom_frame, text="Second parent genome string:")
        self.p2_data = tk.Entry(self.custom_frame, textvariable=self.p2_string)

        self.but__validate = tk.Button(master,
                                       text='Start the game',
                                       command=self.set_result)
        self.max_pop_label.grid(column=0, row=0)
        self.max_pop_data.grid(column=1, row=0)

        self.nb_iter_label.grid(column=0, row=1)
        self.nb_iter_data.grid(column=1, row=1)

        self.graphs_label.grid(column=0, row=2)
        self.graphs_data.grid(column=1, row=2)

        self.verbose_label.grid(column=0, row=3)
        self.verbose_data.grid(column=1, row=3)

        self.session_frame.grid(column=0, row=0)

        self.warning.grid(row=0, column=0)
        self.p1_label.grid(row=1, column=0)
        self.p1_data.grid(row=2, column=0)
        self.p2_label.grid(row=3, column=0)
        self.p2_data.grid(row=4, column=0)

        self.custom_frame.grid(column=1, row=0)
        self.but__validate.grid(column=0, columnspan=2, row=1)
        self.master.mainloop()

    def set_gen_results(self):
        """
        Verify the usability of the entered gen strings and correct them as empty if needed
        """
        value = self.p1_string.get()
        if len(value) != gn.get_max_genome_length():
            self.p1_string.set('')
        else:
            for char in value:
                if char not in ('0', '1'):
                    self.p1_string.set('')
                    break
        value = self.p2_string.get()
        if len(value) != gn.get_max_genome_length():
            self.p2_string.set('')
        else:
            for char in value:
                if char not in ('0', '1'):
                    self.p2_string.set('')
                    break

    def set_result(self):
        """
        Sets the final configuration into the args format used by the main program
        """
        self.set_gen_results()
        self.result = (int(self.max_pop_data.get()),
                       int(self.nb_iter_data.get()),
                       self.do_graphs.get(),
                       self.do_verbose.get(),
                       self.p1_string.get(),
                       self.p2_string.get())
        self.master.destroy()
