#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-04-07
Purpose: Randomly subset a FASTA file
"""

import argparse
import random 
import os
from Bio import SeqIO 
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Probablistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        nargs='+',
                        help='Input FASTA file(s)')

    parser.add_argument('-p',
                        '--pct',
                        help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=0.1)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    if not 0 < args.pct < 1:
        parser.error(f'--pct "{args.pct}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    out_dir = args.outdir
    fasta = args.file 
    seq_total = 0


#    seqs = 0 
    fh_total = 0
    for fh in args.file:
        seqs = 0
        basename = os.path.basename(fh.name)
        out_file = os.path.join(out_dir, basename)
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)
        fh_total += 1         
        print(f'  {fh_total}: {basename}')

        total_files = len(args.file)
        more = 's' if total_files > 1 else ''
            
        out_fh = open(out_file, 'wt')

        for rec in SeqIO.parse(fh, 'fasta'): 
            if random.random() <= args.pct: 
                SeqIO.write(rec, out_fh, 'fasta')
                seqs += 1

        seq_total += seqs
        plural = 's' if seq_total > 1 else ''

        out_fh.close() 
        

    print(f'Wrote {seq_total:,d} sequence{plural} from {fh_total} file{more} to directory "{args.outdir}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
