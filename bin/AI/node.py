"""
This class represents a node, a possibility in the move decision tree search.
"""

import bin.ruleset as rs


class Node:
    def __init__(self, game, player, opponent, move):
        self.game = game
        self.opponent = opponent
        self.player = player
        self.move = move

    def move_set(self):
        """
        Determines every possible moves and returns the exhaustive list

        :return: the exhaustive list of possible moves
        """
        move_set = []
        balls = self.game.get_player_balls(self.game.who_plays())
        for ball in balls:
            for direction in ('l', 'r', 'u', 'd'):
                if rs.can_move(self.game, self.game.who_plays(), ball[0], ball[1], direction,
                               self.player.get_last_moves()):
                    move_set.append((ball[0], ball[1], direction))
        return move_set

    def get_child_node(self, move):
        """
        Returns the next possibility , next Node based on the selected move

        :param move: the selected move
        :return: the new child node
        """
        child_game = self.game.copy()
        child_game.move(move[0], move[1], move[2])
        return Node(child_game, self.opponent, self.player, move)

    def has_ended(self):
        """
        Returns if there is no more child possible from this node

        :return: if the game has ended or not
        """
        return rs.has_ended(self.game)
