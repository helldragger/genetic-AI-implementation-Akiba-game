import bin.input as i
import bin.ruleset as rs


class Player:
    def __init__(self):
        self.__last_moves = [0, 0, 0, 0]
        self.__name = ''

    def which_player(self):
        """
        Returns players own name (might be a depreciated feature soon)

        :return: the players name
        """
        return self.__name

    def update_last_moves(self, move):
        """
        Updates the players last moves with the new last one (might be a depreciated feature soon)

        :param move: the new last move to add to the last moves queue
        """
        del self.__last_moves[0]
        self.__last_moves.append(move)

    def last_move(self):
        """
        Returns the players last move (might be a depreciated feature soon)

        :return: the players last move
        """
        return self.__last_moves[-1]

    def get_last_moves(self):
        """
        Returns the players last moves list (might be a depreciated feature soon)

        :return: the players last moves list
        """
        return self.__last_moves

    def get_move(self, game):
        """
        Asks the user a move until the user returns a correct and possible move

        :param game: the current game object
        :return: the move issued by the player
        """
        move = i.ask_move()
        while not rs.can_move(game, self.__name, move[0], move[1], move[2], self.__last_moves, verbose=True):
            move = i.ask_move()
        self.update_last_moves(move)
        return move

    def set_name(self, role):
        """
        Sets this players name to the new name (might be a depreciated feature soon)

        :param role: the new name of the player (might be 'p1', or 'p2')
        """
        self.__name = role

    def get_name(self):
        """
        Returns this players name (might be a depreciated feature soon)

        :return: this players name
        """
        return self.__name
