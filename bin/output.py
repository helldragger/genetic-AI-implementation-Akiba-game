"""Second layer of abstraction, the interactivity: the output"""

ERR_PREFIX = "ERR "
INF_PREFIX = "INF "


# ####FORMATTING DATA#####

def format_ball(value):
    """
    Format the game ball owner into a specific string

    :param value: the owner of the ball if any
    :return: a string of the forementioned ball

    >>> format_ball('p1')
     p1

    >>> format_ball('p2')
     p2

    >>> format_ball('red')
     re

    >>> format_ball('yolo')
     --

    >>> format_ball(None)
     --

    """
    if value is None:
        return ' -- '
    elif value == 'p1':
        return ' p1 '
    elif value == 'p2':
        return ' p2 '
    elif value == 'red':
        return ' re '
    else:
        return ' -- '


def format_game(game):
    """
    Format the game into a printable string

    :return: the formatted string to print
    """
    formatted_game = "y\\x\t\t  0 \t  1 \t  2 \t  3 \t  4 \t  5 \t  6 "
    for y in range(7):
        formatted_game = "".join([formatted_game, '\n', str(y), '\t'])
        for x in range(7):
            formatted_game = "\t".join([formatted_game, format_ball(game.get_owner(x, y))])
    return formatted_game


def format_error(error):
    """
    Adds a red color to error messages

    :param error: the raw error
    :return: the coloured error
    """
    return '\033[93m' + error + '\033[0m'


def format_info(info):
    """
    Adds a green color to info messages

    :param info: the raw info
    :return: the coloured info
    """
    return '\033[92m' + info + '\033[0m'


# ####PRINTING DATA#####

def print_error(error):
    """
    Prints a coloured console error

    :param error: the raw error to print

    >>> print_error('error')
    ERR  > error

    """
    global ERR_PREFIX
    print(format_error(ERR_PREFIX + " > " + error))


def print_info(info):
    """
    Prints a coloured console info

    :param info: the raw info to print

    >>> print_info('information')
    INF  > information

    """
    global INF_PREFIX
    print(format_error(INF_PREFIX + " > " + info))


def print_game(game):
    """
    Prints the game state to the console
    """
    print(format_game(game))
