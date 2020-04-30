#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-04-29
Purpose: Parsing swissprot records
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
        description='Filter SwissProt file for keywords, taxa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='SwissProt file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keyword to take',
                        metavar='keyword',
                        type=str,
                        default=None)

    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        metavar='[taxa[taxa ...]]',
                        type=str,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')
    
    args = parser.parse_args() 

    if not args.keyword: 
        parser.error('the following arguments are required: -k/--keyword') 
    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    keywords = args.keywords
    skips = 0 

    for rec in SeqIO.parse(args.file, "swiss"): 
        print(rec)
    
    taxonomy = ['Eukaryota', 'Alveolata', 'Apicomplexa', 'Aconoidasida',
        'Haemosporida', 'Plasmodiidae', 'Plasmodium', 'Plasmodium (Plasmodium)']

    taxa = set(map(str.lower, taxonomy)) 
    skip = set(map(str.lower, [args.skip]))
    sharedvalues = skip.intersection(taxa)
    skips += 1
    
    takes = 0
    keywor = [args.keyword] 
    if skip.intersection(taxa) == None: 
        keys = set(map(str.lower, keywor))
        sharedkeys = keywords.intersection(keys)
        SeqIO.write(res, args.outfile, 'fasta') 
        takes += 1

    print(f'Done, skipped {skips} and took {takes}. See output "{args.outfile.name}"') 
# --------------------------------------------------
if __name__ == '__main__':
    main()
