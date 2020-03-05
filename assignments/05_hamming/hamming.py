#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-03-03
Purpose: Rock the Casbah
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='str',
                        type=argparse.FileType('r'),
                        help='Input file',
                        default='')

    parser.add_argument('-m',
                        '--min',
                        help='Minimum Hammer Value',
                        metavar='int',
                        type=int,
                        default=0) 
                       

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.file
   
    for lines in text:
        word_1, word_2 = lines.rstrip().split()        
    
        dist = abs(len(word_1)-len(word_2)) 
        for char1, char2 in zip(word_1, word_2):
            if char1 != char2:
                dist += 1
        if dist >= args.min:    
            print(f'{dist:8}:{word_1:20}{word_2:20}')
            
        
# --------------------------------------------------
if __name__ == '__main__':
    main()
