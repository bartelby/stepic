import argparse
from count_kmers import pattern_count
from count_kmers import read_file

def frequent_patterns(text, k):
    """
    Implementation of a naieve algorithm to find the most frequent k-mers that occur in a text (very slow)
    :param text:
    :param k: length of k-mer
    :return: a list of the 'most frequent' k-mers in a text
    """
    frequent_patterns = set()
    count = {}
    for i in range(len(text)-k):
        pattern = text[i:i+k]
        c = pattern_count(text, pattern)
        if c:
            count.update({i:c})
    maxkey = max_key(count)
    max_count = count.get(maxkey,0)
    for i in range(len(text) - k):
        if count[i] == max_count:
            frequent_patterns.add(text[i:i+k])
    return ' '.join(str(p) for p in list(frequent_patterns))

def max_key(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def get_cli():
    usage = "usage: %(prog)s"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-f", dest="file_name", help="Name of file containing genome.")
    parser.add_argument("-k", dest="k", help='Length of kmer')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_cli()
    file_name = args.file_name
    k = int(args.k)
    text = read_file(file_name)
    fp = frequent_patterns(text, k)
    print fp


