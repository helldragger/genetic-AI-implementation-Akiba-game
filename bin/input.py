"""Second layer of abstraction, the interactivity: input"""

# ####IMPORTATIONS#####
import bin.output as o


# ####USER INPUT VERIFICATION#####

def is_conform_move(move):
    """
    Check if user input does not contain any forbidden character (used for potential serialization) or impossible
    coordinates

    :param move: user input
    :return: if user input is correct or not

    >>> is_conform_move('0 0 d')
    True

    >>> is_conform_move('0 7 d')
    False

    >>> is_conform_move('0 0 e')
    False

    >>> is_conform_move('0 -1 d')
    False

    >>> is_conform_move('0 -1')
    False

    >>> is_conform_move('0 2 du')
    False

    >>> is_conform_move('0 d d')
    False

    """
    if len(move) != 3:
        o.print_error("Unaccepted command, a move must be formatted as '<x> <y> <direction>'")
        return False
    try:
        move[0] = int(move[0])
        move[1] = int(move[1])
    except TypeError:
        o.print_error('Unaccepted coordinates, x and y must be integers')
        return False
    else:
        if 0 <= move[0] <= 6 and 0 <= move[1] <= 6:
            if len(move[2]) > 1:
                o.print_error('Unaccepted direction, must be only one letter as (U)p, (R)ight, (D)own or (L)eft.')
                return False
            for char in move[2]:
                if char not in ('u', 'r', 'd', 'l'):
                    o.print_error(
                        "You used some illegal characters. Try again using only (U)p, (R)ight, (D)own or (L)eft")
                    return False
            return True
        else:
            o.print_error("Coordinates must be between 0 and 6 inclusive")


# ####USER INPUT INTERACTION#####

def get_input():
    """
    Asks input from the user with a nice white prefix

    :return: raw user input
    """
    return input("Player > ").lower().split(' ')


def ask_move():
    """
    Asks the user to issue a move

    :return: move issued
    """
    move = get_input()
    while not is_conform_move(move):
        move = get_input()
    move[0], move[1] = int(move[0]), int(move[1])
    return move
