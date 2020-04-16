#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-04-15
Purpose: Finding the golden egg
"""

import argparse
import os
import re
from Bio import SeqIO
import sys



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--cdhit',
        metavar='cdhit',
        type=argparse.FileType('r'),
        help='Output file from CD-HIT (clustered proteins)',
        default=None)

    parser.add_argument(
         '-p',
         '--proteins',
         type=argparse.FileType('r'),
         help='Proteins FASTA',
         metavar='proteins',                                                
         default=None)

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='outfile',
        type=argparse.FileType('wt'),
        default='unclustered.fa')

    args = parser.parse_args()
    
    if not args.cdhit:                                                                                              parser.error('the following arguments are required: -c/--cdhit') 

    if not args.proteins:
        parser.error('the following arguments are required: -p/--proteins') 

    return args 

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    protein_ids = set() 
    out_fh = args.outfile
    total_lines = 0
    seq_total = 0
    

    for line in args.cdhit:
        lines = 0
        match = re.search(r'>(\d+)', line)
        if match: 
            match_id = match.group(1)
            protein_ids.add(match_id)
            lines += 1
#            print(f'{protein_ids}')
            total_lines += lines
    
    for rec in SeqIO.parse(args.proteins, 'fasta'):
        prot_id = re.sub(r'\|.*', '', rec.id)
        
        pripro = 0   
        if prot_id not in protein_ids:
#             pripro = 0 
             SeqIO.write(rec, args.outfile, 'fasta')
             pripro += 1
        
        seq_total += pripro
     
        unclust = seq_total + total_lines

    print(f'Wrote {seq_total:,d} of {unclust:,d} unclustered proteins to "{args.outfile.name}"')



# --------------------------------------------------
if __name__ == '__main__':
    main()
