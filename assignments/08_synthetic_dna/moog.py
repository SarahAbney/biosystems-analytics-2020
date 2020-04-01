#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-03-31
Purpose: Creating synthetic DNA/RNA sequences 
"""

import argparse
import random
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        help='Output filename',
                        type=str,
                        default='out.fa')

    parser.add_argument('-t',
                        '--seqtype',
                        help='DNA or RNA',
                        metavar='str',
                        type=str,
                        choices=['rna', 'dna'],
                        default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='Number of sequences to create',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='Minimum length',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='Maximum length',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        help='Percent GC',
                        metavar='float',
                        type=float,
                        default=.5)
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')
    

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)
    out_fh = open(args.outfile, 'wt')


    i_total = 0
    for i in range(args.numseqs):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = ''.join(random.sample(pool, k=seq_len)).upper()
        i_total += 1 
        out_fh.write(f'>{i_total} \n{seq} \n')
    
    out_fh.close()

    print(f'Done, wrote {args.numseqs} {args.seqtype} sequences to "{args.outfile}".')


# --------------------------------------------------
def create_pool(pctgc, max_len, seq_type):

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


# --------------------------------------------------
if __name__ == '__main__':
    main()
