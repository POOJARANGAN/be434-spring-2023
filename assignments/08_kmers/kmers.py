#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-03-26
Purpose: Finding Common K-mers
"""

import argparse


def find_kmers(seq, k):
    """ Find k-mers in string """

    num_l = len(seq) - k + 1
    return [] if num_l < 1 else [seq[i:i + k] for i in range(num_l)]


def test_find_kmers():
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find Common K-mers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('FILE1',
                        help='Input File 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    if args.kmer <= 0:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Get common Kmers"""

    args = get_args()
    words1 = {}
    for line in args.FILE1:
        for word in line.split():
            for kmer in find_kmers(word, args.kmer):
                # increment the count of this "kmer" in "words1"
                words1[kmer] = words1.get(kmer, 0) + 1

    words2 = {}
    for line in args.FILE2:
        for word in line.split():
            for kmer in find_kmers(word, args.kmer):
                # increment the count of this "kmer" in "words2"
                words2[kmer] = words2.get(kmer, 0) + 1

    cmn_kmers = set(words1.keys()) & set(words2.keys())

    for kmer in sorted(cmn_kmers):
        print(f'{kmer:<10} {words1[kmer]:>5} {words2[kmer]:>5}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
