"""First layer of abstraction concerning the game state: the rule set"""
import bin.output as o


def who_won(g):
    """
    Returns who won if any

    :param g: the current game
    :return: the player who won if any
    """
    if g.player_balls_left('p2') == 0 or g.red_balls_count('p1') == 6:
        return 'p1'
    elif g.player_balls_left('p1') == 0 or g.red_balls_count('p2') == 6:
        return 'p2'
    else:
        return None


def has_ended(game):
    """
    Returns if the game has been won by any of the two players or the turn timeout has been reached

    :param game: the current game
    :return: if it has ended or not
    """
    return (game.get_turn_count() >= 50) or (game.player_balls_left('p2') == 0 or game.red_balls_count('p1') == 6) or (
        game.player_balls_left('p1') == 0 or game.red_balls_count('p2') == 6)


def can_move(g, p, x, y, d, last_moves, verbose=False):
    """
    Determines if the movement is possible

    :param last_moves: the list of last moves, might be useless
    :param g: the current game
    :param p: the player
    :param x: the X coordinate of the ball
    :param y: the Y coordinate of the ball
    :param d: the direction of the move
    :param verbose: enable debug output or not
    :return: The right to move or not
    """
    if not g.has_ball(x, y):
        if verbose:
            o.print_error("There is no ball here.")
        return False
    elif g.get_owner(x, y) != p:
        if verbose:
            o.print_error("This ball doesn't belong to you!")
        return False

    up, right, down, left = ('u', 'r', 'd', 'l')
    move = (x, y, d)
    # # Si c'est la meme boule que la derniere survivante du dernier mouvement
    # # Si la commande est de repartir en sens inverse, alors non.
    # TODO Determines if necessary or useless
    if move in last_moves:
        if verbose:
            o.print_error("You can't repeat this move.")
        return False

    # espace suffisant ?
    if d == right:
        if g.has_ball(x - 1, y):
            if verbose:
                o.print_error('There is a ball in your way')
            return False
    elif d == up:
        if g.has_ball(x, y + 1):
            if verbose:
                o.print_error('There is a ball in your way')
            return False
    elif d == left:
        if g.has_ball(x + 1, y):
            if verbose:
                o.print_error('There is a ball in your way')
            return False
    elif d == down:
        if g.has_ball(x, y - 1):
            if verbose:
                o.print_error('There is a ball in your way')
            return False

    # sortie de bille alliée
    if d == right and x + 1 == 7:
        if verbose:
            o.print_error("You can't eliminate a ball of yours")
        return False
    elif d == up and y - 1 == -1:
        if verbose:
            o.print_error("You can't eliminate a ball of yours")
        return False
    elif d == left and x - 1 == -1:
        if verbose:
            o.print_error("You can't eliminate a ball of yours")
        return False
    elif d == down and y + 1 == 7:
        if verbose:
            o.print_error("You can't eliminate a ball of yours")
        return False

    ball_chain = g.get_ball_chain(x, y, d)
    decalage = len(ball_chain) - 1
    last_ball_x = x
    last_ball_y = y
    if d == right:
        last_ball_x += decalage
    elif d == left:
        last_ball_x -= decalage
    elif d == down:
        last_ball_y += decalage
    elif d == up:
        last_ball_y -= decalage
    if g.get_owner(last_ball_x, last_ball_y) == p:
        if d == right and last_ball_x >= 6:
            if verbose:
                o.print_error("You can't eliminate a ball of yours")
            return False
        elif d == left and last_ball_x <= 0:
            if verbose:
                o.print_error("You can't eliminate a ball of yours")
            return False
        elif d == up and last_ball_y <= 0:
            if verbose:
                o.print_error("You can't eliminate a ball of yours")
            return False
        elif d == down and last_ball_y >= 6:
            if verbose:
                o.print_error("You can't eliminate a ball of yours")
            return False

    return True


def get_eliminated(g, x, y, d):
    """
    Returns the ball who will be eliminated by the next move

    :param g: the current game
    :param x: the X coordinate of the first pushed ball
    :param y: the Y coordinate of the first pushed ball
    :param d: the direction of the movement
    :return: the last ball of the chain who will also be the one eliminated
    """
    return g.get_ball_chain(x, y, d)[-1]
