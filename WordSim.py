import argparse
import sys

import Globals as g
import Config as c
from CharacterScheme import Scheme
from DynamicTimeWarping import DTW


def main(input_name, k, name_list, output_mode, scheme):
    input_grams = input_name.split()
    input_objs = Scheme.create_representations(input_grams, scheme)
    poke_objs = Scheme.create_representations(name_list, scheme)
    scorer = Scheme.create_similarity_scorer(scheme)

    # Merge Mode
    if output_mode == g.MERGE_MODE:
        for gram in input_objs:
            # Find top matches
            merged_names, top_names = DTW.merge(gram, k, poke_objs)

            # Output
            for merged, orig in zip(merged_names, top_names)[:k]:
                print(gram + " + " + orig + " = " + merged)
    # Match Mode
    else:
        # Find top matches
        top_names = DTW.match(input_objs, k, poke_objs, scorer)

        # Output
        for name in input_objs:
            for match in top_names[name][:k]:
                print(name.name + " -> " + match.name)


def get_names(filename):
    names = []
    processed_names = []
    successful = True

    # Try to open what we think is the name file
    try:
        with open(filename, "r") as in_file:
            names = in_file.readlines()
    except IOError:
        sys.stderr.write("Tried and failed to open \"" + filename)
        successful = False

    # Process name list
    if successful:
        processed_names = [n.rstrip("\n") for n in names]

    return processed_names, successful


# Handle Arguments
if __name__ == '__main__':
    # Arguments:    real_name [--k int] [--name_list file] [--merge]
    parser = argparse.ArgumentParser()
    parser.add_argument("real_name", help="the input string")
    parser.add_argument("--k", help="number of results to return")
    parser.add_argument("--name_file", help="name of file containing words to match against")
    # parser.add_argument("--merge", help="number of results to return", action="store_true")
    # parser.add_argument("--scheme", help="how to match: orth, ipa, jap")
    args = parser.parse_args()

    # Required args and defaults
    input_string = args.real_name
    num_outputs = c.DEFAULT_NUM_OUTPUTS
    name_list_filename = c.DEFAULT_NAME_FILENAME
    mode = g.MATCH_MODE
    scheme = g.ENG_SCHEME

    # Number of outputs
    if args.k:
        k_string = args.k
        if k_string.isdigit():
            num_outputs = int(k_string)
        else:
            sys.stderr.write("k should be an integer. Setting to default: " + c.DEFAULT_NUM_OUTPUTS + "\n")

    # File with strings to match
    if args.name_file:
        name_list_filename = args.name_file
    name_collection, success = get_names(name_list_filename)

    # Mode
    '''
    if args.merge:
        mode = g.MERGE_MODE

    # Character scheme
    if args.scheme and args.scheme in g.SCHEMES:
        scheme = args.scheme
    '''

    if success:
        main(input_string, num_outputs, name_collection, mode, scheme)
