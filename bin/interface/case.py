import tkinter as tk

import bin.interface.background as bg
import bin.ruleset as rs


class Case:
    """
    The case canvas, the canvas instantiated in each plateau's case
    """

    def __init__(self, master, owner, x, y):
        self.cnv = master
        self.__owner = owner
        self.x = x
        self.y = y
        self.selectors = {
            'r': [-90, True],
            'l': [90, True],
            'u': [0, True],
            'd': [180, True]
        }

    def get_current_ball_bg(self):
        """
        returns it's ball based on it's current owner

        :return: an ball to display based on it's current owner
        """
        if self.__owner is None:
            return bg.ball_n
        elif self.__owner == 'red':
            return bg.ball_r
        elif self.__owner == 'p2':
            return bg.ball_b
        elif self.__owner == 'p1':
            return bg.ball_w

    def set_selector_state(self, d, state):
        """
        Sets the state of the specified direction selector.

        :param d: the direction of the selector
        :param state: the state of said selector
        """
        self.selectors[d][1] = state

    def get_selector_state(self, direction):
        """
        Return the desired direction selectors state

        :param direction: the direction of said selector
        :return: the state of the desired selector
        """
        return self.selectors[direction][1]

    def get_selector_bg(self, d):
        """
        returns it's background based on it's current state

        :return: an image to display based on it's current state
        """

        if self.__owner is None:
            return bg.get_selector_image(False, d)
        return bg.get_selector_image(self.get_selector_state(d), d)

    def set_owner(self, owner):
        """
        sets the current owner with the new owner

        :param owner: the new owner
        """
        self.__owner = owner

    def get_owner(self):
        """
        return the current owner

        :return: the current owner
        """
        return self.__owner

    def update(self):
        """
        Update the Case Layer content display
        """
        if self.__owner is None or self.__owner == 'red':
            for direction in ('l', 'r', 'u', 'd'):
                self.set_selector_state(direction, False)
        else:
            inv_dir = {
                'd': 'u',
                'u': 'd',
                'r': 'l',
                'l': 'r'
            }
            for direction in ('l', 'r', 'u', 'd'):
                if rs.can_move(self.cnv.game, self.cnv.game.who_plays(), self.x, self.y, direction,
                               self.cnv.game.get_player(self.cnv.game.who_plays()).get_last_moves()):
                    self.set_selector_state(inv_dir[direction], True)
                else:
                    self.set_selector_state(inv_dir[direction], False)

        self.cnv.create_image(self.x * 32 + 0, self.y * 32, anchor=tk.NW, image=bg.case)
        self.cnv.create_image(self.x * 32 + 0, self.y * 32, anchor=tk.NW, image=self.get_current_ball_bg())

        up = self.get_selector_bg('u')
        down = self.get_selector_bg('d')
        left = self.get_selector_bg('l')
        right = self.get_selector_bg('r')

        self.cnv.create_image(self.x * 32 + 8, self.y * 32, anchor=tk.NW, image=up)
        self.cnv.create_image(self.x * 32 + 8, self.y * 32 + 24, anchor=tk.NW, image=down)
        self.cnv.create_image(self.x * 32, self.y * 32 + 8, anchor=tk.NW, image=left)
        self.cnv.create_image(self.x * 32 + 24, self.y * 32 + 8, anchor=tk.NW, image=right)
