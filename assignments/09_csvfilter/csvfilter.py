#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-04-02
Purpose: Filter a delimited text file
"""

import argparse
import csv
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file',
                        required=True)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        required=True)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    src_val = args.val
    src_column = args.col
    reader = csv.DictReader(args.file, delimiter=str(args.delimiter))

    if src_column:
        if src_column not in reader.fieldnames:
            print(f'--col "{src_column}" not a valid column!', file=sys.stderr)
            print(f'Choose from {", ".join(reader.fieldnames)}')
            sys.exit(1)

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    line_b = 0
    for record in reader:
        txt_val = record.get(
            src_column) if src_column else ' '.join(record.values())

        if re.search(src_val, txt_val, re.IGNORECASE):
            line_b += 1
            writer.writerow(record)

    print(f'Done, wrote {line_b:,} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
