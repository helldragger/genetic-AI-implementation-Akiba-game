"""
AI Data computation layer
"""
import bin.ruleset as rs
import bin.AI.graph.connexity as cx


def heuristic(game, genome_data):
    """
    Calculate the node fitness using it's set of data

    winning conditions (+999):

      - victoire par les rouges
      - victoire par elimination

    losing conditions (-999):

      - Defaite par elimination
      - Defaite par les rouges

    others conditions ([0; 31]):

      - Sur-nombre de boules du joueur
      - Minimum de dispersion des boules du joueur
      - Maximum de dispersion des boules adverses
      - Distance moyenne de centre minimale
      - Peut eliminer des boules rouges ou adverses


    :param game: the node game
    :param genome_data: The AI genome data parsed
    :return: the fitness score
    """
    # Variables and multipliers initialization
    score = 0
    p = game.get_player(game.who_plays())
    if p.get_name() == 'p1':
        pla_left = game.player_balls_left('p1')
        pla_red = game.red_balls_count('p1')
        adv_left = game.player_balls_left('p2')
        adv_red = game.red_balls_count('p2')
    else:
        pla_left = game.player_balls_left('p2')
        pla_red = game.red_balls_count('p2')
        adv_left = game.player_balls_left('p1')
        adv_red = game.red_balls_count('p1')

    mult_pla_left = genome_data['pla balls left']
    mult_adv_left = genome_data['adv balls left']
    mult_pla_red = genome_data['pla red balls']
    mult_adv_red = genome_data['adv red balls']

    mean_dist_from_center = 0
    mult_dist = genome_data['distance']

    last_adv = True if adv_left == 1 else False

    last_pla_red = True if pla_red == 5 else False

    can_adv = 0
    mult_elim_adv = genome_data['can elim adv']

    can_red = 0
    mult_elim_red = genome_data['can elim red']

    pla_grps = cx.get_number_of_groups(game.get_player_balls(p.get_name()))
    mult_pla_grps = genome_data['pla group left']

    adv_grps = cx.get_number_of_groups(game.get_player_balls('p1' if p == 'p2' else 'p2'))
    mult_adv_grps = genome_data['adv group left']

    for ball in game.get_player_balls(p.get_name()):
        x, y = ball
        mean_dist_from_center += (abs(4 - x) ** 2 + abs(4 - y) ** 2) ** 0.5
        for d in ('u', 'r', 'd', 'l'):
            if rs.can_move(game, p, x, y, d, p.get_last_moves()):
                eliminated = rs.get_eliminated(game, x, y, d)
                if eliminated is not None:
                    if eliminated == 'red':
                        can_red += 1
                    else:
                        can_adv += 1

    mean_dist_from_center /= pla_left if pla_left != 0 else 0

    # winning conditions
    if (last_pla_red and can_red == 1) or (last_adv and can_adv == 1) or adv_grps == 0:
        return 999

    # losing conditions
    if pla_left == 0 or adv_red == 6 or pla_grps == 0:
        return -999

    # Proportional conditions
    # # Adverse status:
    score += (1 - (adv_left / 8)) * mult_adv_left
    score += (1 - (adv_red / 5)) * mult_adv_red
    score += (adv_grps/adv_left) * mult_adv_grps
    # # Player status:
    score += (pla_left / 8) * mult_pla_left
    score += (pla_red / 5) * mult_pla_red
    score += (1 - (pla_grps/pla_left)) * mult_pla_grps
    # # Distance status:
    score += (1 - (mean_dist_from_center/(3*(2**0.5)))) * mult_dist
    # # Elimination status:
    score += (can_adv/adv_left) * mult_elim_adv
    score += (can_red/(6-pla_red))*mult_elim_red

    # Ratio conditions
    # # Balls left ratio:
    mult_ball_ratio = genome_data['balls ratio']
    score += (pla_left/adv_left) * mult_ball_ratio
    # # Ball groups ratio:
    mult_grps_ratio = genome_data['group ratio']
    score += (pla_grps/adv_grps) * mult_grps_ratio

    return score
