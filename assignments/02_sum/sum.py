#!/usr/bin/env python3

"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-02-05
Purpose: Python program to Sum one or more integer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('INT',
                        metavar='INT',
                        nargs='+',
                        type=int,
                        help='Numbers to add')

    return parser.parse_args()

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()
    converted_string = [str(i) for i in args.INT]
    sum_string = ' + '.join(converted_string)
    print(f"{sum_string} = {sum(args.INT)}")


# --------------------------------------------------
if __name__ == '__main__':
    main()
