def fuse_groups(clean_group, added_group):
    """
    Fuses two ball groups to avoid any duplicates

    :param clean_group: the already clean group
    :param added_group: the group of new things which might contains duplicates
    :return: the cleanly fused group
    """
    for element in added_group:
        if element not in clean_group:
            clean_group.append(element)
    return clean_group


def explore_group(player_balls, source, visited):
    """
    Explore each neighboring ball to determine which balls are interconnected and returns when the list is complete

    :param player_balls: the player balls
    :param source: the ball we are exploring right now
    :param visited: the already visited balls
    :return: the already visited balls
    """
    visited.append(source)
    if (source[0] - 1, source[1]) in player_balls and (source[0] - 1, source[1]) not in visited:
        visited = fuse_groups(visited, explore_group(player_balls, (source[0] - 1, source[1]), visited))
    if (source[0] + 1, source[1]) in player_balls and (source[0] + 1, source[1]) not in visited:
        visited = fuse_groups(visited, explore_group(player_balls, (source[0] + 1, source[1]), visited))
    if (source[0], source[1] - 1) in player_balls and (source[0], source[1] - 1) not in visited:
        visited = fuse_groups(visited, explore_group(player_balls, (source[0], source[1] - 1), visited))
    if (source[0], source[1] + 1) in player_balls and (source[0], source[1] + 1) not in visited:
        visited = fuse_groups(visited, explore_group(player_balls, (source[0], source[1] + 1), visited))
    return visited


def get_number_of_groups(player_balls):
    """
    Returns the number of ball groups for a player

    :param player_balls: the player's ball coordinates
    :return: the number of groups
    """
    groups = 0
    grouped_balls = []
    while len(player_balls) > len(grouped_balls):
        i = 0
        while player_balls[i] in grouped_balls:
            i += 1
        ball = player_balls[i]
        balls_group = explore_group(player_balls, ball, [])
        fuse_groups(grouped_balls, balls_group)
        groups += 1
    return groups
