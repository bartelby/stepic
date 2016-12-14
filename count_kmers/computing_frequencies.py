# coding=utf-8
import argparse
from count_kmers import read_file
from collections import defaultdict

"""
The pseudocode below generates a frequency array by first initializing every element in
the frequency array to zero (4k operations) and then making a single pass down
Text (approximately |Text| · k operations). For each k-mer Pattern that we encounter, we add 1 to
the value of the frequency array corresponding to Pattern. As before, we refer to the k-mer
beginning at position i of Text as Text(i, k).

    ComputingFrequencies(Text, k)
        for i ← 0 to 4k − 1
            FrequencyArray(i) ← 0
        for i ← 0 to |Text| − k
            Pattern ← Text(i, k)
            j ← PatternToNumber(Pattern)
            FrequencyArray(j) ← FrequencyArray(j) + 1
        return FrequencyArray
"""

bool_val = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}

def compute_frequency_array(text, k):
    """
    :param text:
    :param k: length of k-mer
    :return: An dict showing the number of times each possible k-mer occurs in the text
    """
    #using a default dict eliminates the need to initialize the freq array.
    freq_array = defaultdict(int)
    for i in range(len(text) - k):
        pattern = text[i:i + k]
        j = pattern_to_number(pattern)
        freq_array[j] += 1
    rslt = [freq_array[i] for i in range(4**k)]
    return ' '.join(str(p) for p in rslt)

def pattern_to_number(pattern):
        sbool = ''.join([bool_val[c] for c in pattern.strip()])
        return int(sbool, 2)

def get_cli():
    usage = "usage: %(prog)s"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-f", dest="file_name", help="Name of input file.")
    parser.add_argument('-o', dest='output_file', help="Name of output file")
    parser.add_argument("-t", dest='text', help="text value of genome (short value for testing)")
    parser.add_argument("-k", dest="k", help='Length of kmer')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_cli()
    file_name = args.file_name
    k = int(args.k)
    if file_name:
        text = read_file(file_name)
    else:
        text = args.text
    results = compute_frequency_array(text.strip(), k)
    output_file = args.output_file
    if output_file:
        of = open(output_file, 'w')
        of.write(results + '\n')
        of.close()
    else:
        print results