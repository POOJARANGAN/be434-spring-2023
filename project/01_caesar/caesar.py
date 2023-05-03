#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-04-26
Purpose: FInal Class Project
"""

import argparse


def caesar_shift(message, shift):
    """Encode a message using the Caesar Shift """
    result_out = ''
    for char in message:
        if char.isalpha():
            # Get the ASCII code for the character and shift
            code = ord(char) + shift
            # Wrap around to the start of the alphabet if necessary
            if char.islower():
                if code > ord('z'):
                    code -= 26
                elif code < ord('a'):
                    code += 26
            elif char.isupper():
                if code > ord('Z'):
                    code -= 26
                elif code < ord('A'):
                    code += 26
            # Convert the shifted code back to a character
            result_out += chr(code)
        else:
            # Append non-letter characters unchanged
            result_out += char
    return result_out


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='caesar shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true',
                        default=False)

    parser.add_argument('FILE',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='std.out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Encode or decode a message using the Caesar Shift"""
    args = get_args()
    shift = args.number if not args.decode else -args.number
    message = args.FILE.read().strip()
    encoded = caesar_shift(message, shift)
    args.outfile.write(encoded.upper())
    args.outfile.close()
    print(encoded.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
