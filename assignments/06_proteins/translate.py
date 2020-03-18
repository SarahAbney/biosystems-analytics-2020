#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-03-17
Purpose: Proteins!
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequences', metavar='str', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        metavar='FILE',
        type=argparse.FileType('r'),
        required=True,
        default='None')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename',
        metavar='FILE',
        type=str,
        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """If you only saw how much I had commented out....#RIP"""

    args = get_args()
    seq = args.sequences
    lookup = {}
    answers = ''
    out_fh = open(args.outfile, 'wt')



    for line in args.codons:
        codon, protein = line.split()
        lookup[codon] = protein



    for i in range(0, len(args.sequences), 3):
             protein_seq = args.sequences.upper()[i:i + 3]
             answers += lookup.get(protein_seq, "-") 


    out_fh.write(answers)


    out_fh.close()

    print(f'Output written to "{args.outfile}".')
# --------------------------------------------------
if __name__ == '__main__':
    main()
