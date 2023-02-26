#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-02-22
Purpose: translate DNA/RNA
"""

import argparse

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        type=str,
                        help='Input file(s)')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations (default: None)',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        required=True)
    # action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename (default: out.txt)',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    codons_dict = {}

    for line in args.codons:
        key, value = line.rstrip().split()
        codons_dict[key] = value

    k = 3
    seq = args.str

    list_s = []
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        list_s.append(codons_dict.get(codon.upper(), '-'))

    print(f'Output written to "{args.outfile.name}".')

    with open(args.outfile.name, 'wt', encoding="utf-8") as fh_open:
        fh_open.write(''.join(list_s))

    # fh_open = open(args.outfile.name, 'wt')
    # fh_open.write(''.join(list_s))
    # fh_open.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
