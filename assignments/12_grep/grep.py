#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-04-22
Purpose: Python Grep using Named Tuple
"""

import re
import argparse
from typing import NamedTuple


class MatchedLine(NamedTuple):
    """
        Match line for grep
    """
    file: str
    line_num: int
    line: str
    original_line: str


def grep(regex, a_f, case_sensitive=True, out_f=None, print_o=False):
    """
        Match pattern from input files
    """
    files = [MatchedLine(file.name, i+1, line.strip(), line.strip())
             for file in a_f for i, line in enumerate(file, start=0)]
    if not case_sensitive:
        regex = re.compile(regex, re.IGNORECASE)
    else:
        regex = re.compile(regex)

    matched_lines = set()
    for file in files:
        with open(file.file, encoding='utf-8') as fl_inp:
            for i, line in enumerate(fl_inp, start=1):
                matches = regex.finditer(line)
                for match in matches:
                    start, end = match.span()
                    matched_text = match.group()
                    original_line = line.rstrip('\n')
                    matched_line = line[:start] + matched_text + line[end:]
                    if len(a_f) == 1:
                        matched_line = f'{matched_line}'
                    if len(a_f) > 1:
                        matched_line = f'{file.file}:{matched_line}'
                    matched = MatchedLine(
                        file.file, i, matched_line, original_line)
                    if matched not in matched_lines:
                        matched_lines.add(matched)
                        if out_f:
                            out_f.write(f'{matched_line.strip()}\n')
                        if print_o:
                            print(f'{matched_line.strip()}')


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        default=False,
                        action='store_true')

    parser.add_argument('PATTERN',
                        help='Search pattern',
                        metavar='PATTERN',
                        type=str)

    parser.add_argument('FILE',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help="Output (default: <_io.TextIOWrapper"
                        "name= '<stdout>' mode='w' encoding='utf-8'>)",
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        default='-')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    a_f = args.FILE
    regex = args.PATTERN

    case_sensitive = not args.insensitive
    out_f = args.outfile

    print_o = not out_f
    grep(regex, a_f, case_sensitive, out_f, print_o)


if __name__ == '__main__':
    main()
