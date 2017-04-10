"""
The main plateau, the main display and interactivity
"""
import tkinter as tk

from bin.interface.case import Case


class Plateau(tk.Canvas):
    """
    The frame containing every case canvas
    """

    def __init__(self, master, game):
        super(Plateau, self).__init__(master, width=224, height=224)
        self.game = game
        self.__plateau = {}

    def get_selector_state(self, x, y, d):
        """
        Returns the state of the corresponding move selector of the corresponding case

        :param x: x coordinate of the case
        :param y: y coordinate of the case
        :param d: the direction of the selector
        :return: the state of the selector
        """
        if self.__plateau.get((x, y)) is not None:
            return self.__plateau.get((x, y)).get_selector_state(d)
        return False

    def new_game(self):
        """
        Generate the whole grid of cases
        """
        grid = {}
        for x in range(7):
            for y in range(7):
                if (x, y) in self.game.get_player_balls('p1'):
                    grid[(x, y)] = Case(self, 'p1', x, y)
                elif (x, y) in self.game.get_player_balls('p2'):
                    grid[(x, y)] = Case(self, 'p2', x, y)
                elif (x, y) in self.game.get_player_balls('red'):
                    grid[(x, y)] = Case(self, 'red', x, y)
                else:
                    grid[(x, y)] = Case(self, None, x, y)
                grid[(x, y)].update()
        self.__plateau = grid

    def update_grid(self):
        """
        Displays the whole grid state
        """
        for x in range(7):
            for y in range(7):
                if (x, y) in self.game.get_player_balls('p1'):
                    self.__plateau[(x, y)].set_owner('p1')
                elif (x, y) in self.game.get_player_balls('p2'):
                    self.__plateau[(x, y)].set_owner('p2')
                elif (x, y) in self.game.get_player_balls('red'):
                    self.__plateau[(x, y)].set_owner('red')
                else:
                    self.__plateau[(x, y)].set_owner(None)
                self.__plateau[(x, y)].update()
