import math

from bin.AI.heuristics import heuristic


def negamax_alpha_beta(node, depth, alpha, beta, player, genome_data):
    """

    For each node/situation, calculate every move possible and reaction possible

        1.  Player situation node, score is unknown
        2.  List every moves possible by the player, giving the adversary an unknown reaction score
        3.  List every move possible by the adversary, giving another player unknown score

        If calculus depth is reached (max iteration):

            1.  Calculate the fitness of every possible move by the player

            (Assuming the adversary will play perfectly)

            2.  Sets every possible adversary move score = -min(player_moves[0], ..., player_moves[i])
            3.  Sets every possible player move score = max(-adversary_moves[0], ..., -adversary_moves[i])

            Repeat until root situation score is set

            4.  Returns the move corresponding to

    :param node: the current explored node
    :param depth: the current depth
    :param alpha: the current node alpha
    :param beta: the current node beta
    :param player: who plays determine the multiplier
    :param genome_data: the current node genome data
    :return: the best move possible
    """
    move_set = node.move_set()
    if depth == 0 or node.has_ended() or len(move_set) == 0:
        return [node.move, player * heuristic(node.game, genome_data)]
    best_score = -math.inf
    best_move = ()
    for move in move_set:
        if best_move == ():
            best_move = move
        child_node = node.get_child_node(move)
        child_result = negamax_alpha_beta(child_node, depth - 1, -alpha, -beta, -player, genome_data)
        score = -child_result[1]

        if score >= best_score:
            best_score = score
            best_move = move
        alpha = max(alpha, score)
        if alpha >= beta:
            break
    return [best_move, best_score]
