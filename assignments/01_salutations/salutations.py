#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-02-01
Purpose: Print greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print greeting',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        metavar='str',
                        type=str,
                        default='Stranger')

    parser.add_argument('-e',
                        '--excited',
                        help='A boolean flag for excitement',
                        action='store_true'
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Greetings and salutations"""

    args = get_args()

    if args.excited:
        print(f'{args.greeting}, {args.name}!')
    else:
        print(f'{args.greeting}, {args.name}.')


# --------------------------------------------------
if __name__ == '__main__':

    main()
