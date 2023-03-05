#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-03-04
Purpose: Expand DNA IUPAC Codes
"""

import argparse

# --------------------------------------------------


def iupac_to_regex(iupac_code):
    """
       Converts an IUPAC code to a regular expression.

       Parameters:
           iupac_code (str): The IUPAC code to convert.

       Returns:
           str: The regular expression corresponding to the IUPAC code.
       """
    iupac_regex = {
        "A": "A",
        "C": "C",
        "G": "G",
        "T": "T",
        "U": "U",
        "R": "[AG]",
        "Y": "[CT]",
        "S": "[GC]",
        "W": "[AT]",
        "K": "[GT]",
        "M": "[AC]",
        "B": "[CGT]",
        "D": "[AGT]",
        "H": "[ACT]",
        "V": "[ACG]",
        "N": "[ACGT]"
    }
    regex = []
    for base in iupac_code:
        regex.append(iupac_regex[base.upper()])
    return regex

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPSC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('SEQ',
                        metavar='SEQ',
                        type=str,
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help="Output filename (default: <_io.TextIOWrapper"
                        "name= '<stdout>' mode='w' encoding='utf-8'>)",
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default='-')

    return parser.parse_args()

# --------------------------------------------------


def main():
    """Make a jazz noise here"""

    args = get_args()

    for iupac_code in args.SEQ:
        regex_list = iupac_to_regex(iupac_code)
        regex = "".join(regex_list)
        output_string = iupac_code + ' ' + regex
        print(output_string, file=args.outfile)

    if args.outfile.name != '<stdout>':
        print(f'Done, see output in "{format(args.outfile.name)}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
