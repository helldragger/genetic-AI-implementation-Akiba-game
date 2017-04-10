"""Last layer of abstraction, the coordination: the main loop"""

import bin.AI.bot as bot
import bin.AI.training as tr
import bin.game as g
import bin.gui as gui
import bin.output as o
import bin.player as player
import bin.ruleset as rs


def gui_mode(adv_is_bot, adv_genome):
    """
    Runs the gui mode

    :param adv_is_bot: determines if p2 is human (class Player) or a bot (Player subclass bot.AI)
    :param adv_genome: if p2 is a bot, adv_genome contains the bot's genome
    """
    gui.GUI(adv_is_bot, adv_genome)


def training_mode(max_pop, iterations, graphs, verbose, p1_gen, p2_gen):
    """
    Runs the training mode

    :param max_pop: the maximum size of the population
    :param iterations: the maximum number of generations
    :param graphs: if we must display graphs on the fly or not
    :param verbose: if we must display generation progression or not in the console
    :param p1_gen: if not empty, contains a custom first parent genome
    :param p2_gen: if not empty, contains a custom second parent genome
    """
    tr.Training(max_pop=max_pop, nb_iterations=iterations, graphs=graphs, verbose=verbose, p1_gen=p1_gen, p2_gen=p2_gen)


def command_line_mode(adv_is_bot, adv_genome):
    """
    Runs the command-line mode

    :param adv_is_bot: determines if p2 is human (class Player) or a bot (Player subclass bot.AI)
    :param adv_genome: if p2 is a bot, adv_genome contains the bot's genome
    """
    p1 = player.Player()

    if adv_is_bot:
        p2 = bot.AI(gen=adv_genome)
    else:
        p2 = player.Player()

    game = g.Game(p1=p1, p2=p2)
    game.run()

    if game.get_turn_count() >= 50:
        o.print_info("Ex aequo!")
    else:
        o.print_info(rs.who_won(game) + ' has won!')

    return


def run(mode, args):
    """
    Runs the main loop of the game
    """
    if mode == 'commandline':
        return command_line_mode(args[0], args[1])
    elif mode == 'gui':
        return gui_mode(args[0], args[1])
    elif mode == 'training':
        return training_mode(args[0], args[1], args[2], args[3], args[4], args[5])
