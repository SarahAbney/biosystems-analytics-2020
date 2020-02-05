#!/usr/bin/env python3
"""
Author : Seabney
Date   : 20200204
Purpose: Python program to write a Python program
"""

import argparse 
import sys 
import os 


# --------------------------------------------------
def get_args():
    """Get arguments"""

    parser = argparse.ArgumentParser(
        description='Crows nest',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metvar='str', help='A word')

    return parser.parse_args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word

    print(f'Ahoy, Captain, ' + word + ' off the larboard bow') 

# --------------------------------------------------
if __name__ == '__main__':
    main()



