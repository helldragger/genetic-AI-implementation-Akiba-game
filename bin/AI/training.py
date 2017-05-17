"""
The AI training module.
"""
import bin.AI.bot as bot
import bin.AI.genetics as gene
import bin.database.genobase as gb
import bin.game as g
import bin.output as o


def generate_pop(current_pop, size):
    """
    Fill the current population to the determined size with fully random individuals

    :param current_pop: the current population queue
    :param size: the current population queue size
    :return: the completed list
    """
    current_size = len(current_pop)
    for _ in range(size - current_size):
        rand_genetic = gene.gen_rand_genome()
        current_pop.append(bot.AI(gen=rand_genetic))
    return current_pop


def generate_games(pop):
    """
    Generates a tournament for every individual to battle against every others

    :param pop: the population
    :return: the game list
    """
    games_list = []
    for i in range(len(pop) - 1):
        for j in range(i + 1, len(pop)):
            game = g.Game(p1=pop[i], p2=pop[j], verbose=False)
            games_list.append(game)
    return games_list


def selection(population, scores):
    """
    Determines the best players with the simple medium strategy

    :param population: the players
    :param scores: the scores of every players
    :return: the 2 best players
    """
    players_medium_scores = []
    # players medium score determination
    for player in population:
        p_scores = scores[player]
        p_medium_score = 0
        for score in p_scores:
            p_medium_score += score
        p_medium_score /= len(p_scores)
        players_medium_scores.append((player, p_medium_score))
    # best 2 scores determination
    first_player, first_score = (0, -999999)
    second_player, second_score = (0, -999999)
    for p, med_score in players_medium_scores:
        if med_score > first_score or first_score == -999999:
            second_player = first_player
            second_score = first_score
            first_score = med_score
            first_player = p
        elif med_score > second_score or second_score == -999999:
            second_score = med_score
            second_player = p
    return [[first_player, second_player], [first_score, second_score]]


def session(parents, max_pop, graphs, verbose):
    """
    Operates a full session from a certain population or not.

    ..#. Generates population
    ..#. Generate games with generated population
    ..#. Run every games
    ..#. When every game has finished: get every player score
    ..#. Epurate the population to keep the best of them

    :param parents: the former population if any
    :return: the best players of the current session
    """
    pop_size = max_pop
    scores = {}
    # Generate population
    pop = []
    if parents is not None:
        if len(parents) > max_pop:
            raise ValueError('Too much population')
        for p in parents:
            pop.append(p)
    pop = generate_pop(pop, pop_size)
    for player in pop:
        scores[player] = []
    # Generate games
    games = generate_games(pop)
    # Run every games until finished and then get scores
    c = 1
    total_games = len(games)
    for game in games:
        if verbose:
            o.print_info('\tCurrent game analysis: ' + str(c) + '\t / \t' + str(total_games))
        c += 1
        game.run()
        p1 = game.get_player('p1')
        p2 = game.get_player('p2')
        p1.calculate_score(game)
        p2.calculate_score(game)
        scores[p1].append(p1.get_score())
        scores[p2].append(p2.get_score())
    # Manipulate some data for the sake of graphics (mmh dope graphics! <3) (min, max, mean, etc...)
    # if graphs:
    #     foo = 'bar'
    # Epurate generation
    results = selection(pop, scores)
    return results


class Training:
    def __init__(self, max_pop, nb_iterations, graphs, verbose, p1_gen, p2_gen):
        parents = []
        if p1_gen != '':
            parents.append(bot.AI(gen=p1_gen))
        if p2_gen != '':
            parents.append(bot.AI(gen=p2_gen))
        if nb_iterations == 0:
            gen = 0
            while True:
                o.print_info('Current generation: ' + str(gen + 1))
                results = session(parents, max_pop, graphs, verbose)
                gb.dump_generations(results, max_pop, nb_iterations, gen + 1)
                parents = results[0]
                gen += 1
        else:
            for gen in range(nb_iterations):
                o.print_info('Current generation: ' + str(gen + 1))
                results = session(parents, max_pop, graphs, verbose)
                gb.dump_generations(results, max_pop, nb_iterations, gen+1)
                parents = results[0]
