#! /usr/bin/python3
# Author: Pablo Baeyens
# Usage:
#   ./$0 -h
# for usage info and options

import editdistance
import argparse
import os.path


def load(name):
    """Loads list of words"""
    with open(name) as dictionary:
        return dictionary.read().splitlines()


def closest(query, dictionary, n):
    """Gets n closest words to query using editdistance"""
    return sorted(dictionary,
                  key=lambda word: editdistance.eval(query, word))[:n]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Finds list of words closest to a given one using edit distance")
    parser.add_argument("dictionary", help="List of words (one per line)")
    parser.add_argument("word", help="Query word")
    parser.add_argument(
        "--n",
        nargs=1,
        help="Number of results",
        metavar="NUM",
        default=['10'])
    args = parser.parse_args()

    try:
        dictionary = load(args.dictionary)
    except FileNotFoundError:
        print("'{}' is not a valid filename".format(args.dictionary), end="")
        if os.path.exists(args.word):
            print(
                ", but '{}' is.\nDid you write the arguments in the wrong order?".format(
                    args.word))
        else:
            print("")
        exit(-1)

    try:
        n = int(args.n[0])
    except ValueError:
        print("Malformed argument '--n {}'".format(args.n[0]))
        exit(-1)

    matches = closest(args.word, dictionary, n)

    print("Closest words to '{}':".format(args.word))
    for n, w in enumerate(matches, start=1):
        print(n, w)
