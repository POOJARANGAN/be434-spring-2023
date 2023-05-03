#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-04-27
Purpose: Basic Substitution Cipher
"""

import argparse
import random


def create_sub_table(seed=None):
    """Scramble alphabet to create a random substitution table"""

    # Create list of alphabet
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

    # Shuffle using the provided seed
    if seed is not None:
        random.seed(seed)
    shuffled_alphabet = random.sample(alphabet, len(alphabet))

    # map letter to a shuffled letter to create a sub table
    sub_table = dict(zip(alphabet, shuffled_alphabet))

    return sub_table


def sub_cipher(message, sub_table):
    """Substitution cipher - Encode/decode a message"""

    # replace each ltr to create the encoded/decoded
    # from the sub table
    result_out = ''
    for char in message:
        if char.isalpha():
            # Replace the message from the sub table
            if char.islower():
                result_out += sub_table[char]
            else:
                result_out += sub_table[char.lower()].upper()
        else:
            # Append non-ltr char unchanged
            result_out += char

    return result_out

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='substituition cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='A random seed',
                        metavar='SEED',
                        type=int,
                        default=3)

    parser.add_argument('FILE',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true',
                        default=False)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='std.out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print output"""

    args = get_args()

    # Create the substitution table
    sub_table = create_sub_table(args.seed)

    # Read the input message from the input file
    message = args.FILE.read().strip()

    # Encode or decode the message using the substitution cipher
    if args.decode:
        encoded = sub_cipher(
            message, {v: k for k, v in sub_table.items()})
    else:
        encoded = sub_cipher(message, sub_table)

    # Write the encoded message to the output file
    args.outfile.write(encoded.upper())
    print(encoded.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
