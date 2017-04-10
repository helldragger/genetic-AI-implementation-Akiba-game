"""
Contains the Player subclass bot.AI, used to overwrite the user get_move without over-complicating the code and is
used to define the way the AI is working
"""

import bin.AI.genetics as gene
import bin.AI.negamax as nega
from bin.AI.node import Node
from bin.player import Player


class AI(Player):
    def __init__(self, gen='', identity=None):
        Player.__init__(self)
        self._id = identity
        if gen == '':
            gen = gene.gen_rand_genome()
        self.gen_string = gen
        self.__gen = gene.read_genome(gen)
        self.fitness_score = 0

    def get_move(self, game):
        """
        Tests the game to get the best move possible in a minimal amount of time and decides it based on the AI genome

        :param game: the current game
        :return: the move decided by the AI
        """
        game.disable_verbose()
        depth = 10
        opponent = game.get_player('p2' if game.who_plays() == 'p1' else 'p1')

        best_move = nega.negamax_alpha_beta(Node(game.copy(), self, opponent, opponent.last_move()), depth, -99999,
                                            2, 1, self.__gen)
        move = best_move[0]
        self.update_last_moves(move)
        game.enable_verbose()
        return move

    def calculate_score(self, game):
        """
        Calculate the definitive score of the AI in the ended game

        :param game: the current game
        """
        self.fitness_score = gene.fitness(self, game)

    def printable_results(self):
        """
        Returns a readable string containing the AI final performance and it's genome for reference

        :return: the AI fitness score and genome in a pretty formatted string
        """
        return ''.join(['Fitness score : ', str(self.fitness_score), '\n genome: ', str(self.gen_string)])

    def get_score(self):
        """
        Returns the AI calculated final fitness score

        :return: this AI latest fitness score
        """
        return self.fitness_score

    def copy(self):
        """
        Returns a copy of itself

        :return: a copy of itself
        """
        return AI(gen=self.gen_string)

    def get_id(self):
        """
        Returns this AI identity (might be a depreciated feature soon)

        :return: this AI identity
        """
        return self._id

    def get_gen_string(self):
        return self.gen_string
