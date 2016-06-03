import re
import Globals as g
import Config as c
from CharacterScheme.SchemeObjects import *


def create_representations(name_list, scheme):
    if scheme == g.ENG_SCHEME:
        representation_list = english_representation(name_list)

    elif scheme == g.ORTH_SCHEME or scheme == g.JAP_SCHEME:
        representation_list = [Representation(p, p.lower()) for p in name_list]

    else:
        representation_list = [Representation(p, p) for p in name_list]

    return representation_list


def english_representation(name_list):
    compressed_words = []

    for name in name_list:
        rep = name.lower()

        # convert "y"
        pre_y = r"(^|" + g.CONSONANT_PATTERN + r")"
        post_y = r"(" + g.CONSONANT_PATTERN + r"|$)"
        y_pattern = pre_y + "y" + post_y
        rep = re.sub(y_pattern, r"\1i\2", rep)

        # convert consonants
        rep = convert_eng_consonants(rep)

        poke = Representation(name, rep)
        compressed_words.append(poke)

    return compressed_words


def convert_eng_consonants(word):
    # Chunks to probable pronunciation
    for chunk in g.ENG_CHUNKS:
        word = re.sub(chunk, g.ENG_CHUNKS[chunk], word)

    # Compress duplicates
    double_pattern = r"(" + g.CONSONANT_PATTERN + r")\1"
    word = re.sub(double_pattern, r"\1", word)

    return word


def create_similarity_scorer(scheme):
    similarity_scorer = {}

    if scheme == g.ENG_SCHEME:
        similarity_scorer = eng_similarity_scheme()

    return similarity_scorer


def eng_similarity_scheme():
    sim_scorer = {}

    sim_scorer[g.VOWEL] = {}
    sim_scorer[g.VOWEL][g.VOWEL] = c.VV
    sim_scorer[g.VOWEL][g.CONSONANT] = c.VC
    sim_scorer[g.VOWEL][g.EMPTY] = c.VE

    sim_scorer[g.CONSONANT] = {}
    sim_scorer[g.CONSONANT][g.VOWEL] = c.VC
    sim_scorer[g.CONSONANT][g.CONSONANT] = c.CC
    sim_scorer[g.CONSONANT][g.EMPTY] = c.CE

    return sim_scorer


def char_type(char):
    type = g.CONSONANT

    is_vowel = re.match(g.VOWEL_PATTERN, char)
    if is_vowel:
        type = g.VOWEL

    return type


def char_similarity_score(char_1, char_2, similarity_scorer):
    return similarity_scorer[char_1.type][char_2.type]
