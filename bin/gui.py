"""
The third layer of abstraction, a graphical interface
"""

import tkinter as tk
from tkinter import messagebox

import bin.game as g
import bin.interface.background as bg
import bin.ruleset as rs
from bin.interface.command import CommandUI
from bin.interface.plateau import Plateau
from bin.interface.scoreboard import StateUI
import bin.AI.bot as bot


class GUI(tk.Tk):
    """
    Load up images in memory, create the main window and adds each panel, binds the main event to the game and starts it
    """

    def __init__(self, adv_is_bot, adv_genome):
        super(GUI, self).__init__()
        bg.load_images()
        if adv_is_bot:
            self.game = g.Game(p2=bot.AI(gen=adv_genome))
        else:
            self.game = g.Game()

        self.against_bot = adv_is_bot

        self.UI = tk.Frame(self)
        self.UI.grid()

        # State frame
        self.state_frame = StateUI(self.UI, self.game)
        self.state_frame.grid(row=2, column=0)
        # Game canvas
        self.game_canvas = Plateau(self.UI, self.game)
        self.game_canvas.grid(row=1, column=0)
        # Command frame
        self.command_frame = CommandUI(self.UI, self)
        self.command_frame.grid(row=0, column=0)

        self.game_canvas.bind("<Button-1>", self.clicked_at)

        self.new_game()
        self.mainloop()

    def new_game(self):
        """
        Resets the game and the UI
        """
        self.game.new_game()
        self.game_canvas.new_game()
        self.state_frame.reset_scoreboard()

    def clicked_at(self, click):
        """
        Here, the input is processed in several steps:

        1. Get the case with coordinates // 32.
        2. Get the location of the mouse inside the case with % 32
        3. Determine the Direction clicked with a little hitbox of 8x16 pixel on each side.
        4. If a selector has been clicked, verify if it is activated. If not, the input is ignored
        5. Else we send the input to the game
        6. We update_game the game state
        7. Update of the screen
        8. Wait for next input!

        :param click: The click event
        """
        direction = None
        x = click.x
        y = click.y
        coord = (x // 32, y // 32)
        x %= 32
        y %= 32
        if 0 <= x < 8 <= y < 24:
            direction = 'l'
        elif 24 > x >= 8 > y >= 0:
            direction = 'u'
        elif 8 <= x < 24 <= y < 32:
            direction = 'd'
        elif 32 > x >= 24 > y >= 8:
            direction = 'r'
        if direction is not None:
            if self.game_canvas.get_selector_state(coord[0], coord[1], direction):
                inv_dir = {
                    'd': 'u',
                    'u': 'd',
                    'r': 'l',
                    'l': 'r'
                }
                player = self.game.who_plays()
                self.game.move(coord[0], coord[1], inv_dir[direction])

                self.state_frame.update_scoreboard()
                self.game_canvas.update_grid()

                if rs.who_won(self.game) == player:
                    messagebox.showinfo(player + " won!", player + " won in" + str(self.game.get_turn_count()) + " turns!")
                    self.new_game()

                elif self.against_bot:
                    player = self.game.who_plays()
                    mv = self.game.get_player(player).get_move(self.game)
                    self.game.move(mv[0], mv[1], mv[2])
                    self.state_frame.update_scoreboard()
                    self.game_canvas.update_grid()
                    if rs.who_won(self.game) == player:
                        messagebox.showinfo(player + " won!", player + " won in" + str(self.game.get_turn_count()) + " turns!")
                        self.new_game()
