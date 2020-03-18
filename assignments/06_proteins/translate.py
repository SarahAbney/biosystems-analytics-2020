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

    parser.add_argument('sequences',
                        metavar='str',
                        help='DNA/RNA sequence')
   
    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True,
                        default='None')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=str,
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.sequences
    lookup = {lines[0:3].upper(): lines[3:].upper().split() for lines in args.codons}
   
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    for i in range(0,len(args.sequences),3):
        protein_seq = args.sequences.upper()[i:i+3] 
 
#        print(protein_seq)
#        print(lookup) 

        if protein_seq in lookup:
            print(*lookup[protein_seq], end = "")
        else: 
            print('-', end = "")
               # print(protein_seq)
       # else: 
        #    print('-')
 
   # for i in range(0, len(seq), 3): 
    #    protein_seq += args.codons[seq[i:i+3]] 
   # print(protein_seq)

   # out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout 
   # for protein_seqs in args.sequences:
      #  [seq[i:i + k] for i in range(0, len(seq) - k + 1, k)]:
      #  if protein_seqs.upper() in lookup: 
       #     print(lookup[protein_seqs.upper()])
   # print(protein_seqs.upper()) 

       # else:
        #    print(f'-')
            
        out_fh.write() 
    out_fh.close() 
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
