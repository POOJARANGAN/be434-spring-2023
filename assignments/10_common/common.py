#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-04-08
Purpose: Find Common Words
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find Common Words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help="Output filename (default: <_io.TextIOWrapper"
                        "name= '<stdout>' mode='w' encoding='utf-8'>)",
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default='-')

    parser.add_argument('FILE1',
                        help='Input File 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        help='Input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Get common words"""

    args = get_args()

    # empty dictionary
    words1 = {}
    for line in args.FILE1:
        for word in line.split():
            words1[word] = words1.get(word, 0)

    words2 = {}
    for line in args.FILE2:
        for word in line.split():
            words2[word] = words2.get(word, 0)

    # find words
    cmn_words = set(words1.keys()) & set(words2.keys())

    # Write the common words to the output, if provided
    if args.outfile:
        with args.outfile as file_out:
            for word in sorted(cmn_words):
                file_out.write(word + '\n')

    else:
        for word in sorted(cmn_words):
            print(word)


# --------------------------------------------------
if __name__ == '__main__':
    main()
