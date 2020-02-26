#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-02-25
Purpose: Head Banger
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
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Input File',
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        nargs='+',
                        help='Number of Lines',
                        metavar='str',
                        type=str,
                        default=10)

    args = parser.parse_args()
        
    return args


# --------------------------------------------------
def main():
    """Tell me what I want to hear"""

    args = get_args()
    
    
    print(open(args.file).read.rstrip()[0:args.num]) 

# --------------------------------------------------
if __name__ == '__main__':
    main()
