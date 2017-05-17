"""Hard coded moves, no abstraction, no rules, the hard layer."""
import copy

import bin.output as o
import bin.player as pl
import bin.ruleset as rs


def new_data():
    """
    Initialize a new plateau to play on
    """
    return {
        # Black balls

        'p1':  [(0, 0), (1, 0), (0, 1), (1, 1), (5, 5), (5, 6), (6, 5), (6, 6)],

        # White balls

        'p2':  [(0, 5), (0, 6), (1, 5), (1, 6), (5, 0), (5, 1), (6, 0), (6, 1)],

        # Red balls

        'red': [(3, 1), (2, 2), (3, 2), (4, 2), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (2, 4), (3, 4), (4, 4), (3, 5)]

    }


# INITIALIZATION
class Game:
    def __init__(self, data=None, players=None, p1=None, p2=None, curr_p='p1', turn_c=0, ball_c=None, red_c=None,
                 verbose=True):
        if data is None:
            self._data = new_data()
        else:
            self._data = data

        if ball_c is None:
            self._balls_count = {
                'p1':  8,
                'p2':  8,
                'red': 13
            }
        else:
            self._balls_count = ball_c

        if red_c is None:
            self._red_count = {
                'p1': 0,
                'p2': 0
                }
        else:
            self._red_count = red_c

        self._turns_count = turn_c
        self._current_player = curr_p
        self._players = {}
        if players is None:
            if p1 is None:
                self._players['p1'] = pl.Player()
                self._players['p1'].set_name('p1')
            else:
                self._players['p1'] = p1
                self._players['p1'].set_name('p1')
            if p2 is None:
                self._players['p2'] = pl.Player()
                self._players['p2'].set_name('p2')
            else:
                self._players['p2'] = p2
                self._players['p2'].set_name('p2')
        else:
            self._players = players
        self._verbose = verbose

    def enable_verbose(self):
        """
        Enable command line output for this game
        """
        self._verbose = True

    def disable_verbose(self):
        """
        Disable command line output for this game
        """
        self._verbose = False

    def copy(self):
        """
        Returns a real modifiable and independent copy of this game object

        :return: a deep copy of this game instance
        """
        return copy.deepcopy(self)

    def new_game(self):
        """
        Initialize a new plateau to play on
        """
        self._data = new_data()

    # DATA GETTERS

    def get_game(self):
        """
        Returns a copy of the state of the game
    
        :return: a copy of the game data
        """
        return self._data.copy()

    def get_turn_count(self):
        """
        Returns the number of turns played during this game
    
        :return: the amount of turns played during this game
        """
        return self._turns_count

    def who_plays(self):
        """
        Returns whose player have to play next
    
        :return: next player
        """
        return self._current_player

    def update_turn(self):
        """
        Update the next player to have to play and the amount of turns played
        """
        if self._current_player == 'p2':
            self._current_player = 'p1'
            self._turns_count += 1
        else:
            self._current_player = 'p2'

    def get_owner(self, x, y):
        """
        Returns the ownership of the corresponding coordinates
    
        :param x: the x coordinate to look at
        :param y: the y coordinate to look at
        :return: the ownership of this case
    
        >>> game=Game();game.new_game();game.get_owner(0,0)
        'p1'
    
        >>> game=Game();game.new_game();game.get_owner(3,3)
        'red'
    
        >>> game=Game();game.new_game();game.get_owner(1,2)
        None
    
        >>> game=Game();game.new_game();game.get_owner(0,5)
        'p2'
    
        """
        if (x, y) in self._data['p1']:
            return 'p1'
        elif (x, y) in self._data['p2']:
            return 'p2'
        elif (x, y) in self._data['red']:
            return 'red'
        else:
            return None

    def get_ball_chain(self, x, y, d):
        """
        Returns the ordered list of balls affected by the movement from the closer to the farther
    
        :param x: the x coordinate at the beginning
        :param y: the y coordinate at the beginning
        :param d: the direction of the movement
        :return: a list of balls ownerships affected by the movement
    
    
        >>> game=Game();game.new_game();game.get_ball_chain(0,0,'r')
        ['p1','p1']
    
        >>> game=Game();game.new_game();game.get_ball_chain(0,1,'r')
        ['p1']
    
        >>> game=Game();game.new_game();game.get_ball_chain(1,2,'d')
        []
    
        """
        up, right, down, left = ('u', 'r', 'd', 'l')
        chain = []

        if d == up:
            for y in range(y, -1, -1):
                if (x, y) in self._data['p1']:
                    chain.append('p1')
                elif (x, y) in self._data['p2']:
                    chain.append('p2')
                elif (x, y) in self._data['red']:
                    chain.append('red')
                else:
                    break
        elif d == right:
            for x in range(x, 7):
                if (x, y) in self._data['p1']:
                    chain.append('p1')
                elif (x, y) in self._data['p2']:
                    chain.append('p2')
                elif (x, y) in self._data['red']:
                    chain.append('red')
                else:
                    break
        elif d == down:
            for y in range(y, 7):
                if (x, y) in self._data['p1']:
                    chain.append('p1')
                elif (x, y) in self._data['p2']:
                    chain.append('p2')
                elif (x, y) in self._data['red']:
                    chain.append('red')
                else:
                    break
        elif d == left:
            for x in range(x, -1, -1):
                if (x, y) in self._data['p1']:
                    chain.append('p1')
                elif (x, y) in self._data['p2']:
                    chain.append('p2')
                elif (x, y) in self._data['red']:
                    chain.append('red')
                else:
                    break
        return chain

    def player_balls_left(self, p):
        """
        Returns the amount of balls remaining for player p
    
        :param p: the player
        :return: the amount of ball remaining for the player
    
        >>> game=Game();game.new_game();game.player_balls_left('p1')
        8
    
        """
        return self._balls_count[p]

    def get_player(self, name):
        """
        returns the corresponding player data

        :param name: the name of the player
        :return: the player data
        """
        return self._players[name]

    def get_player_balls(self, name):
        """
        returns the list of named player position

        :param name: the name of the player
        :return: his balls position
        """
        return self._data[name]

    def get_red_balls(self):
        """
        Returns the list of red balls positions

        :return: the red balls positions
        """
        return self._data['red']

    def red_balls_left(self):
        """
        Returns the amount of red balls remaining
    
        :return: the amount of red balls remaining
    
    
        >>> game=Game();game.new_game();game.red_balls_left()
        13
    
        """
        return self._balls_count['red']

    def red_balls_count(self, p):
        """
        Returns the amount of red balls the player has eliminated during the game
    
        :param p: the player
        :return: the amount of red balls the player has eliminated
    
        >>> game=Game();game.new_game();game.red_balls_count('p1')
        0
    
        """
        return self._red_count[p]

    def has_ball(self, x, y):
        """
        Returns if there is an ownership on a case or not

        :param x: the x coordinate of the case
        :param y: the y coordinate of the case
        :return: if it does belong to someone

        >>> game=Game();game..new_game();game.has_ball(0,0)
        'p1"

        >>> game=Game();game.new_game();game.has_ball(4,4)
        'red'

        >>> game=Game();game.new_game();game.has_ball(0,3)
        None

        >>> game=Game();game.new_game();game.has_ball(6,0)
        'p2'
        """
        return (x, y) in self._data.get('p1') + self._data.get('p2') + self._data.get('red')

    def can_reach(self, xs, ys, xt, yt, d):
        """
        Returns if there is a continuity of balls between two balls

        :param xs: source ball x coordinate
        :param ys: source ball y coordinate
        :param xt: target ball x coordinate
        :param yt: target ball y coordinate
        :param d: the direction of the move
        :return: if it is possible

        >>> game=Game();game.new_game();game.can_reach(0,0,0,1,'d')
        True

        >>> game=Game();game.new_game();game.can_reach(0,0,0,1,'r')
        False

        >>> game=Game();game.new_game();game.can_reach(0,0,5,0,'d')
        False

        """
        up, right, down, left = ('u', 'r', 'd', 'l')
        data = self._data.get('p1') + self._data.get('p2') + self._data.get('red')
        if (d == right or d == left) and ys == yt:
            for xi in range(min(xs, xt), max(xs, xt)):
                if (xi, ys) not in data:
                    return False
            return True
        elif (d == down or d == up) and xs == xt:
            for yi in range(min(ys, yt), max(ys, yt)):
                if (xs, yi) not in data:
                    return False
            return True
        return False

    # MECHANICS

    def move_ball(self, player, old_pos, new_pos):
        """
        Moves a ball from the old pos to the new_pos

        :param player: the owner of the ball
        :param new_pos: the new position
        :param old_pos: the old position
        """
        for i in range(len(self._data[player])):
            if self._data[player][i] == old_pos:
                self._data[player][i] = new_pos
                break

    def remove_ball(self, owner, pos):
        """
        Removes the specified ball from the game and player's index

        :param owner: the owner of the ball
        :param pos: the position (x,y) of the ball
        """
        index = 0
        for i in range(len(self._data[owner])):
            if self._data[owner][i] == pos:
                index = i
                break
        del self._data[owner][index]
        self._balls_count[owner] -= 1
        if owner == 'red':
            self._red_count[self._current_player] += 1

    def move(self, x, y, d):
        """
        Moves a ball in the wanted direction if possible.
    
        :param x: the X coordinate of the ball to move
        :param y: the Y coordinate of the ball to move
        :param d: The direction of the movement
        """
        up, right, down, left = ('u', 'r', 'd', 'l')

        ball_queue = self.get_ball_chain(x, y, d)
        decal = len(ball_queue) - 1
        last_ball_x = x
        last_ball_y = y
        if d == right:
            last_ball_x += decal
        elif d == left:
            last_ball_x -= decal

        if d == down:
            last_ball_y += decal
        elif d == up:
            last_ball_y -= decal
        if (d == up and last_ball_y == 0) or (d == left and last_ball_x == 0) or (d == right and last_ball_x == 6) or (
                        d == down and last_ball_y == 6):
            self.remove_ball(self.get_owner(last_ball_x, last_ball_y), (last_ball_x, last_ball_y))
            ball_queue.pop(-1)

        for balls_done in range(len(ball_queue)):
            decal = len(ball_queue) - 1
            if d == up:
                old_pos = (x, y - decal + balls_done)
                new_pos = (x, y - decal + balls_done - 1)
            elif d == down:
                old_pos = (x, y + decal - balls_done)
                new_pos = (x, y + decal - balls_done + 1)
            elif d == left:
                old_pos = (x - decal + balls_done, y)
                new_pos = (x - decal + balls_done - 1, y)
            else:
                old_pos = (x + decal - balls_done, y)
                new_pos = (x + decal - balls_done + 1, y)

            ball_owner = self.get_owner(old_pos[0], old_pos[1])
            self.move_ball(ball_owner, old_pos, new_pos)
        self.update_turn()

    # Main function

    def run(self):
        """
        Lets the game run itself until completion

        :return: the final state of the game
        """
        p1_turn = True

        if self._verbose:
            o.print_game(self)
        while not rs.has_ended(self):
            if p1_turn:
                mv = self.get_player('p1').get_move(self.copy())
            else:
                mv = self.get_player('p2').get_move(self.copy())
            if self._verbose:
                o.print_info(self._current_player + ' move is ' + str(mv))
            if mv != ():
                self.move(mv[0], mv[1], mv[2])
            else:
                o.format_info("No moves possibles")
            if self._verbose:
                o.print_game(self)
            p1_turn = not p1_turn

        return self
