# coding=utf-8
import argparse

"""
The goal is to generate the d-neighborhood Neighbors(Pattern, d), the set of all k-mers whose
Hamming distance from Pattern does not exceed d.
"""

bases = ["A","C","T","G"]

def neighbors(pattern, d):
    """
    Note that this is a recursive algorithm.  It may be difficult to implement recursively
    in python as tail recursion is not supported. This means that for deep recursions,
    the stack is likely to blow up.

    Neighbors(Pattern, d)
        if d = 0
            return {Pattern}
        if |Pattern| = 1
            return {A, C, G, T}
        Neighborhood ← an empty set
        SuffixNeighbors ← Neighbors(Suffix(Pattern), d)
        for each string Text from SuffixNeighbors
            if HammingDistance(Suffix(Pattern), Text) < d
                for each nucleotide x
                    add x • Text to Neighborhood
            else
                add FirstSymbol(Pattern) • Text to Neighborhood
        return Neighborhood
    :param pattern:
    :param d:
    :return:
    """
    if d == 0:
        return {pattern}
    elif len(pattern) == 1:
        return {'A','C','T','G'}
    neighborhood = {None}
    suffix_neighbors = neighbors(suffix(pattern), d)
    for txt in suffix_neighbors:
        if txt and hamming_distance(suffix(pattern), txt) < d:
            for base in bases:
                neighborhood.add(base + txt)
        elif txt:
            neighborhood.add(pattern[0] + txt)
    neighborhood.remove(None)
    return neighborhood

def neighbors_iterative(pattern, d):
    """
    Here is an Iterative algorithm for finding neighbors - compare results and running time to recursion
    IterativeNeighbors(Pattern, d)
        Neighborhood ← set consisting of single string Pattern
        for j = 1 to d
            for each string Pattern’ in Neighborhood
                add ImmediateNeighbors(Pattern') to Neighborhood
                remove duplicates from Neighborhood
        return Neighborhood
    :param pattern:
    :param d:
    :return:
    """
    neighborhood = {pattern}
    for j in range(d):
        accumulator = {None}
        for neighbor in neighborhood:
            nextdoor_neighbors = immediate_neighbors(neighbor)
            for nextdoor_neighbor in nextdoor_neighbors:
                accumulator.add(nextdoor_neighbor)
        for a in accumulator:
            if a:
                neighborhood.add(a)
    return neighborhood

def immediate_neighbors(pattern):
    """
    First generate the 1-neigborhood of Pattern using the following pseudocode:

    ImmediateNeighbors(Pattern)
        Neighborhood ← the set consisting of single string Pattern
        for i = 1 to len(Pattern)
            symbol ← i-th nucleotide of Pattern
            for each nucleotide x different from symbol
                Neighbor ← Pattern with the i-th nucleotide substituted by x
                add Neighbor to Neighborhood
        return Neighborhood

    Example: ACG Should return  ACG    CCG    GCG    TCG    AAG    AGG    ATG    ACA    ACC    ACT
    :param pattern:
    :return: a set of 'neighbor' patterns - kmers identical to pattern except for one base.
    """
    neighborhood = {pattern} # A set whose first element is pattern.
    for i in range(len(pattern)):
        symbol = pattern[i]
        for base in bases:
            if symbol != base:
                word = list(pattern)  #Strings are immutable - to substitute a letter,
                                      # convert to a list, substitute the letter and make a new string.
                word[i] = base
                neighborhood.add(''.join(word))
    return neighborhood

def suffix(pattern):
    """
    If we remove the first symbol of Pattern (denoted FirstSymbol(Pattern)),
    then we will obtain a (k − 1)-mer that we denote by Suffix(Pattern).
    :param pattern:
    :return: all but the first character of pattern or an empty array
    """
    return pattern[1:]

def hamming_distance(s1, s2):
    """
    The 'Hamming distance' between two strings of equal length is the number of positions at which
    the corresponding symbols are different.
    :param s1: A string
    :param s2: Another string of length equal to s1
    :return: Hamming dist. btw. two strings or None if the strings are unequal length.
    """
    if s1 and s2 and len(s1) == len(s2):
        return sum([1 if  s1[i] != s2[i] else 0 for i in range(0, len(s1))])
    else:
        return None


def get_cli():
    usage = "usage: %(prog)s"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-p", dest="pattern", help="The pattern.")
    parser.add_argument("-d", dest="d", help="Maximum Hamming distance betwen neighbors")
    parser.add_argument("-f", dest='f', help="Output File Name")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_cli()
    pattern = args.pattern
    d = args.d
    f = args.f
    neighbors = neighbors(pattern, d)
    if f:
        with open(f, 'w') as the_file:
            for neighbor in neighbors:
                the_file.write(neighbor + "\n")
    else:
        for neighbor in neighbors:
            print neighbor
