#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-02-09
Purpose: Solfege
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        nargs='+',
                        help='Solfege')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    solfege = {'Do': 'A deer, a female deer',
                     'Re': 'A drop of golden sun',
                     'Mi': 'A name I call myself',
                     'Fa': 'A long long way to run',
                     'Sol': 'A needle pulling thread',
                     'La': 'A note to follow sol',
                     'Ti': 'A drink with jam and bread'}

    for key in args.str:
        if key in solfege:
            print(f'{key}, {solfege[key]}')
        else:
            print(f"I don't know \"{key}\"")


# --------------------------------------------------
if __name__ == '__main__':
    main()
