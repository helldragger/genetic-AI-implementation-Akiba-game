import random as rand

import bin.ruleset as rs
_gene_length = 5
_gene_max = 2**_gene_length - 1
_gene_names =  ('distance',
                'pla balls left',
                'adv balls left',
                'pla red balls',
                'adv red balls',
                'pla group left',
                'adv group left',
                'can elim red',
                'can elim adv',
                'last adv',
                'balls ratio',
                'group ratio')
_gene_quantity = len(_gene_names)
_mutation_rate = 5/(_gene_length*_gene_quantity)
_mutation_chance = 75/100


def int_to_gen_string(nb):
    """
    Transcript the genome variable from int to a 3-char binary string

    :param nb: the number
    :return: the string
    """
    if nb > _gene_max:
        raise ValueError('multiplier above 31')
    elif nb < 0:
        raise ValueError('multiplier under 0')
    binary = bin(nb)
    string = ''.join(['0' * (_gene_length - len(str(binary)[2:])), str(binary)[2:]])
    return string


def fitness(bot, game):
    """
    Generates a score based on the final state of the game played by the AI

    :param bot: the AI object
    :param game: the game the AI played in
    :return: the fitness score
    """
    score = 0
    p = bot.which_player()
    adv = 'p2' if bot.which_player() == 'p1' else 'p1'
    # Score who won

    winner = rs.who_won(game)
    if winner is None:
        score += 15
    elif winner == bot.get_name():
        score += 30
    else:
        score += 0

    # Score TIME
    score += 50 / (game.get_turn_count() ** (1 / 2))

    # Score total elimination
    score += 10 / (game.player_balls_left(adv) + 6 - game.red_balls_count(p) + 1)

    # Score total resistance
    score += 2 * (game.player_balls_left(p))

    return score


def cross_over(gen_a, gen_b):
    """
    Cross over 2 different genetics to create a new genetic

    :param gen_a: the first parent
    :param gen_b: the second parent
    :return: a new genetic
    """
    gen_c = ''
    for i in range(len(gen_a)):
        if (-1) ** i == 1:
            gen_c = ''.join([gen_c, gen_a[i]])
        else:
            gen_c = ''.join([gen_c, gen_b[i]])
    return gen_c


def mutation(gen_s):
    """
    if there is a mutation, the returned genome is mutated with a certain mutation rate

    :param gen_s: the source genome
    :return: the definitive genome
    """
    if rand.randint(1, 100) > _mutation_chance*100:
        return gen_s
    gen_m = ''
    for i in range(len(gen_s)):
        if rand.randint(0, 100) <= _mutation_rate*100:
            if gen_s[i] == '1':
                gen_m = ''.join([gen_m, '0'])
            else:
                gen_m = ''.join([gen_m, '1'])
        else:
            gen_m = ''.join([gen_m, gen_s[i]])
    return gen_m


def trans_genome(multipliers):
    """
    Transcript multiple multipliers from integers into binary into gen_string

    multipliers:

      - mult_ratio_groups: heuristic multiplier for the ratio between player's and adverse's groups
      - mult_ratio_balls: heuristic multiplier for the ratio between player's and adverse's balls
      - mult_last_pla: heuristic multiplier for the fact there is only one player ball left
      - mult_last_adv: heuristic multiplier for the fact there is only one adverse ball left
      - mult_last_red: heuristic multiplier for the fact there is only one red ball left
      - mult_can_elim_adv: heuristic multiplier for the possibility to eliminate adverse balls
      - mult_can_elim_red: heuristic multiplier for the possibility to eliminate red balls
      - mult_red_groups: heuristic multiplier for the red groups left value
      - mult_adv_groups: heuristic multiplier for the adverse groups left value
      - mult_pla_groups: heuristic multiplier for the player groups left value
      - mult_adv_red: heuristic multiplier for the red balls eliminated by the adverse
      - mult_pla_red: heuristic multiplier for the red balls eliminated by the player
      - mult_adv_left: heuristic multiplier for the adverse balls left value
      - mult_pla_left: heuristic multiplier for the player balls left value
      - mult_dist: heuristic multiplier for the mean distance between the balls and the center of the game

    :return: a gen_string genome
    """
    genome = ''
    for value in multipliers:
        genome = ''.join([genome, int_to_gen_string(value)])
    return genome


def read_genome(gen):
    """
    Transcript from gen_string to a genome dict

    :param gen: the gen_string genome
    :return: the genome dictionary
    """

    genome = {}
    for i in range(0, len(gen), _gene_length):
        genome[_gene_names[i//_gene_length]] = int(gen[i:i+_gene_length], 2)
    return genome


def gen_rand_genome():
    """
    Generates a whole random gen_string genome

    :return: a random genome string
    """
    values = []
    for _ in range(_gene_quantity):
        values.append(rand.randint(0, _gene_max))
    return trans_genome(values)


def get_max_genome_length():
    """
    :return: The total size of a genome
    """
    return _gene_length * _gene_quantity
