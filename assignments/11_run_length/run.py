#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-04-16
Purpose: Run-length encoding/data compression of DNA
"""

import argparse
import os


def rle(seq):
    """ Create RLE """

    # create a string
    sequence = ""
    # start counting
    count_num = 1
    current_char = seq[0]
    # Loop over the sequence from the second character
    for char in seq[1:]:
        # If same character then count
        if char == current_char:
            count_num += 1
        # If different append the count and character to the sequence
        else:
            sequence += current_char if count_num == 1 else current_char + \
                str(count_num)
            # Reset the count and character
            count_num = 1
            current_char = char
    # Append all
    sequence += current_char if count_num == 1 else current_char + \
        str(count_num)
    return sequence


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        type=str,
                        help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if os.path.isfile(args.str):
        with open(args.str, encoding='utf-8') as file_inp:
            for seq in file_inp:
                print(rle(seq.strip()))

    else:
        for seq in args.str.splitlines():
            print(rle(seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
