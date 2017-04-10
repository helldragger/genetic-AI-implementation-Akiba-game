import tkinter as tk

from PIL import ImageTk

import bin.interface.background as bg


class StateUI(tk.LabelFrame):
    """
    The score board who will display the current game state.
    """

    def __init__(self, gui, game):
        tk.LabelFrame.__init__(self, gui, text='Scoreboard', width=750, height=150)
        self.game = game

        self.p1_r_count = tk.IntVar(value=0)
        self.p1_w_count = tk.IntVar(value=8)
        self.p2_r_count = tk.IntVar(value=0)
        self.p2_b_count = tk.IntVar(value=8)
        self.turn_count = tk.IntVar(value=1)

        self.is_p1_turn = ImageTk.PhotoImage(bg.i_is_p1_turn)
        self.not_p1_turn = ImageTk.PhotoImage(bg.i_not_p1_turn)
        self.is_p2_turn = ImageTk.PhotoImage(bg.i_is_p2_turn)
        self.not_p2_turn = ImageTk.PhotoImage(bg.i_not_p2_turn)

        self.ball_r = ImageTk.PhotoImage(bg.i_ball_r)
        self.ball_b = ImageTk.PhotoImage(bg.i_ball_b)
        self.ball_w = ImageTk.PhotoImage(bg.i_ball_w)

        self.p1_turn = tk.Canvas(self, width=256, height=130)
        self.p1_turn.create_image(0, 0, anchor=tk.NW, image=self.is_p1_turn)
        self.p2_turn = tk.Canvas(self, width=256, height=130)
        self.p2_turn.create_image(0, 0, anchor=tk.NW, image=self.not_p2_turn)

        self.p1_left_logo = tk.Canvas(self, width=32, height=32)
        self.p2_left_logo = tk.Canvas(self, width=32, height=32)
        self.p1_left_logo.create_image(0, 0, anchor=tk.NW, image=self.ball_w)
        self.p2_left_logo.create_image(0, 0, anchor=tk.NW, image=self.ball_b)

        self.p1_red_logo = tk.Canvas(self, width=32, height=32)
        self.p2_red_logo = tk.Canvas(self, width=32, height=32)
        self.p1_red_logo.create_image(0, 0, anchor=tk.NW, image=self.ball_r)
        self.p2_red_logo.create_image(0, 0, anchor=tk.NW, image=self.ball_r)

        self.p1_left_data = tk.Label(self, textvariable=self.p1_w_count)
        self.p2_left_data = tk.Label(self, textvariable=self.p2_b_count)

        self.p1_red_data = tk.Label(self, textvariable=self.p1_r_count)
        self.p2_red_data = tk.Label(self, textvariable=self.p2_r_count)

        self.turn_label = tk.Label(self, text="Turn ")
        self.turn_data = tk.Label(self, textvariable=self.turn_count)

        self.p1_turn.grid(row=0, column=0, rowspan=3)

        self.turn_label.grid(row=0, column=1, columnspan=2)
        self.turn_data.grid(row=0, column=3, columnspan=2)

        self.p1_left_logo.grid(row=1, column=1)
        self.p1_left_data.grid(row=1, column=2)
        self.p1_red_logo.grid(row=2, column=1)
        self.p1_red_data.grid(row=2, column=2)

        self.p2_left_logo.grid(row=1, column=4)
        self.p2_left_data.grid(row=1, column=3)
        self.p2_red_logo.grid(row=2, column=4)
        self.p2_red_data.grid(row=2, column=3)

        self.p2_turn.grid(row=0, column=5, rowspan=3)

    def update_players_turn(self):
        """
        Updates the turn state display
        """
        if self.game.who_plays() == 'p1':
            self.p1_turn.create_image(0, 0, anchor=tk.NW, image=self.is_p1_turn)
            self.p2_turn.create_image(0, 0, anchor=tk.NW, image=self.not_p2_turn)
        else:
            self.p1_turn.create_image(0, 0, anchor=tk.NW, image=self.not_p1_turn)
            self.p2_turn.create_image(0, 0, anchor=tk.NW, image=self.is_p2_turn)
        self.turn_count.set(self.game.get_turn_count() + 1)

    def update_score(self):
        """
        Updates the scoreboard display
        """
        self.p1_w_count.set(len(self.game.get_player_balls('p1')))
        self.p1_r_count.set(self.game.red_balls_count('p1'))
        self.p2_b_count.set(len(self.game.get_player_balls('p2')))
        self.p2_r_count.set(self.game.red_balls_count('p2'))

    def update_scoreboard(self):
        """
        Update the whole game state display
        """
        self.update_players_turn()
        self.update_score()

    def reset_players_turn(self):
        """
        Resets the player turns display to the new game state
        """
        self.p1_turn.create_image(0, 0, anchor=tk.NW, image=self.is_p1_turn)
        self.p2_turn.create_image(0, 0, anchor=tk.NW, image=self.not_p2_turn)

    def reset_scoreboard(self):
        """
        Resets the score board as a whole
        """
        self.reset_players_turn()
        self.update_score()
