#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-02-25
Purpose: Head Banger
"""

import argparse
import os
import io
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-n',
                        '--num',
                        help='Number of Lines',
                        metavar='int',
                        type=int,
                        default=10)
    
    parser.add_argument('file',                                                                          metavar='FILE',                                                                  help='Input File',) 

    args = parser.parse_args()

    if not args.num > 0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args 

# --------------------------------------------------
def main():
    """Tell me what I want to hear"""

    args = get_args()

    for i in range(args.num): 
        with open(args.file) as inputfile:
            header = inputfile.read().splitlines()[i]    
        print(f'{header}') 


# --------------------------------------------------
if __name__ == '__main__':
    main()
