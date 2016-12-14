import argparse

def read_file(f):
    return open(f).read()

def pattern_count(text, pattern):
    """
    :param text: example: ATCATGATG
    :param pattern: example: ATG
    :return:  The number of occurrences of the pattern in the text.  Example 3 (given above values for text and pattern)
    """
    count = 0
    for i in range(0, len(text) - len(pattern)):
        if text[i: i + len(pattern)] == pattern:
            count += 1
    return count

def get_cli():
    usage = "usage: %(prog)s"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-f", dest="file_name", help="Name of file containing genome.")
    parser.add_argument("-p", dest="pattern", help="Pattern to search fo in file")

    args = parser.parse_args()
    return args

if __name__=='__main__':
    args = get_cli()
    file_name=args.file_name
    pattern=args.pattern
    text = read_file(file_name)
    count = pattern_count(text, pattern)
    print count