#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-02-16
Purpose: Concatenate Files
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        default=False,
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for file_obj in args.FILE:

        if args.number:
            line_num = 1

        for line in file_obj:
            if args.number:
                print(f'{line_num:>6}\t{line.rstrip()}')
                line_num += 1
            else:
                print(line.rstrip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
