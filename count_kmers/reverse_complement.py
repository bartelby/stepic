import argparse

def reverse_complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement.get(base, base) for base in reversed(seq))

def get_cli():
    usage = "usage: %(prog)s"
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument("-s", dest="seq", help="Sequence to complement.")
    args = parser.parse_args()
    return args

if __name__=='__main__':
    args = get_cli()
    seq = args.seq
    print reverse_complement(seq)

