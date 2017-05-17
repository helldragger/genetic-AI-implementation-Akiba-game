"""
Choose to use JSON instead of pickle or home made serializing to allow more flexibility to manual data manipulation
and more reliability.
If you want to look at a home made database de/serializing module I made, please, have a look into my contact
database project on the forge.
"""

import json
import os


__database_path = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir, "resources/database"))


def format_generation_to_json(gen_list):
    """
    Returns a writable generation list

    :param gen_list: the raw generation data
    :return: the file writable data
    """
    data = {}
    for i in range(len(gen_list[0])):
        ai, score = gen_list[0][i], gen_list[1][i]
        data[i] = {
            'mean fitness': score,
            'genome':       ai.get_gen_string()
        }
    return data


def dump_generations(generation_list, max_pop, nb_it, gen):
    """
    Writes the list of genome and associated fitness score at the end of dated file

    :param generation_list: the list of tuples (generation number, fitness, genome)
    """
    data = format_generation_to_json(generation_list)
    best_score = 0
    for key in data.keys():
        if data[key]['mean fitness'] >= best_score:
            best_score = data[key]['mean fitness']

    with open(__database_path
                      + '\\'
                      +str(gen)
                      +'_on_'
                      +str(nb_it)
                      +'-max_pop_of_'
                      + str(max_pop)
                      +'-best_score_of_'
                      +str(best_score)
                      +'.json',
              'w') as output:
        json.dump(data, output)
