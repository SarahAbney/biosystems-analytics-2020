#!/usr/bin/env python3
"""
Author : Sarah Abney
Date   : 5 Feburary 2020
Purpose: Homework 1 
"""

import argparse
import os
import sys



# --------------------------------------------------
def get_args():
    """Get arguments"""

    parser = argparse.ArgumentParser(
        description="Homework1",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('vowel', 
                        metavar='vowel',
                        help='vowel = A vowel to search for', 
                        type=str, 
                        choices= ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    parser.add_argument('text',
                        metavar='text',
                        help='text= The text to show')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The fun stuff"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    
    if vowel in text:
        print(f'Found "{vowel}" in "{text}" at index {text.index(vowel)}.')
    else: 
        print(f'"{vowel}" is not found in "{text}".')
   
# --------------------------------------------------
if __name__ == '__main__':
    main()
