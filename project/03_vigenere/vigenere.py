#!/usr/bin/env python3
"""
Author : poojarangan <poojarangan@localhost>
Date   : 2023-05-01
Purpose: Vigenere Cipher
"""

import argparse


def encode_vigenere(message, keyword):
    """Use Vigenere cipher to encode a message"""
    enc = []
    index_num = 0
    for letter in message:
        if letter.isalpha():
            key_ltr = keyword[index_num % len(keyword)]
            key_index = ord(key_ltr.upper()) - ord('A')
            message_index = ord(letter.upper()) - ord('A')
            enc_index = (message_index + key_index) % 26
            enc_ltr = chr(enc_index + ord('A'))
            enc.append(enc_ltr)
            index_num += 1
        else:
            enc.append(letter)
    return ''.join(enc)


def decode_vigenere(message, keyword):
    """Decode message"""
    dcd = []
    index_num = 0
    for letter in message:
        if letter.isalpha():
            key_ltr = keyword[index_num % len(keyword)]
            key_index = ord(key_ltr.upper()) - ord('A')
            message_index = ord(letter.upper()) - ord('A')
            dcd_index = (message_index - key_index) % 26
            dcd_ltr = chr(dcd_index + ord('A'))
            dcd.append(dcd_ltr)
            index_num += 1
        else:
            dcd.append(letter)
    return ''.join(dcd)


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='vigenere cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-k',
                        '--keyword',
                        metavar='KEYWORD',
                        help='A keyword',
                        default='CIPHER')

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
    """Make a jazz noise here"""

    args = get_args()

    keyword = args.keyword

    if args.decode:
        cipher_func = decode_vigenere
    else:
        cipher_func = encode_vigenere

    with args.FILE as fh_in, args.outfile as fh_out:
        for line in fh_in:
            result = cipher_func(line, keyword)
            fh_out.write(result.strip() + '\n')
            print(result.upper().strip())


# --------------------------------------------------
if __name__ == '__main__':
    main()
