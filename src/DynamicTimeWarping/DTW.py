from DynamicTimeWarping.DTWObjects import *
import Globals as g
from CharacterScheme.SchemeObjects import Character
from CharacterScheme import Scheme


def match(input_objs, k, poke_name_objs, scorer):
    top_matches = {}     # {input : [top matching pokenames]}
    scores = {}          # {real_name : {poke_name : score}}

    # Find scores
    for input_obj in input_objs:
        scores[input_obj] = {}
        for poke_obj in poke_name_objs:
            scores[input_obj][poke_obj] = normal_DTW(input_obj.representation, poke_obj.representation, scorer)

    # Get best scores
    for input_obj in scores:
        top_list = sorted(scores[input_obj], key=scores[input_obj].get, reverse=True)[:k]
        top_matches[input_obj] = top_list

    return top_matches


def merge(real_name, k, name_list):
    top_matches = []
    merged_names = []

    # TODO -- Merge Mode

    return merged_names, top_matches


def normal_DTW(input_word, poke, scorer):
    input_grams, poke_grams = get_characters(input_word, poke)

    lattice = [[Node() for _ in range(len(poke_grams))] for _ in range(len(input_grams))]
    lattice[0][0].score = 0

    score = simple_score(lattice, input_grams, poke_grams, scorer)
    return score


def get_characters(input_word, poke):
    input_grams = []
    poke_grams = []
    input_grams.append("_")
    poke_grams.append("_")

    for char in list(input_word):
        char_obj = Character(char, Scheme.char_type(char))
        input_grams.append(char_obj)

    for char in list(poke):
        char_obj = Character(char, Scheme.char_type(char))
        poke_grams.append(char_obj)

    return input_grams, poke_grams


def simple_score(lattice, input_grams, poke_grams, sim_scorer):
    for i_index, i in enumerate(input_grams):
        for p_index, p in enumerate(poke_grams):
            node = lattice[i_index][p_index]

            # Grab upper node
            if i_index != 0:
                top_node = lattice[i_index-1][p_index]
                score = top_node.score + sim_scorer[i.type][g.EMPTY]
                if score > node.score:
                    node.score = score
                    location = (i_index-1, p_index)
                    node.backpath = list(top_node.backpath)
                    node.backpath.append(location)

            # Grab left node
            if p_index != 0:
                left_node = lattice[i_index][p_index-1]
                score = left_node.score + sim_scorer[p.type][g.EMPTY]
                if score > node.score:
                    node.score = score
                    location = (i_index, p_index-1)
                    node.backpath = list(left_node.backpath)
                    node.backpath.append(location)

            # Grab diagonal
            if i_index != 0 and p_index != 0:
                diag_node = lattice[i_index-1][p_index-1]
                score = diag_node.score + compare_chars(i, p, sim_scorer)
                if score > node.score:
                    node.score = score
                    location = (i_index-1, p_index-1)
                    node.backpath = list(diag_node.backpath)
                    node.backpath.append(location)

    return lattice[len(input_grams)-1][len(poke_grams)-1].score


def compare_chars(char1, char2, sim_scorer):
    if char1.orth == char2.orth:
        if char1.type == g.CONSONANT:
            score = c.SAME_CONSONANT
        else:
            score = c.SAME_VOWEL
    else:
        score = sim_scorer[char1.type][char2.type]
    return score
