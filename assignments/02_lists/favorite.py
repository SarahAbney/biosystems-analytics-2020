#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-02-11
Purpose: I have a lot of favorite things
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Favorite Things',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('things',
                        metavar='str',
                        nargs='+',
                        help='Some things')

    parser.add_argument('-s',
                        '--sep',
                        help='A separator',
                        metavar='str',
                        type=str,
                        default=', ')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The fun stuff"""

    args = get_args()
    things = args.things
    num = len(things) 
    sep = args.sep

    if num == 1: 

        print(f'{args.things[0]}\nThis is one of my favorite things.') 
    else:
        print('{}\nThese are a few of my favorite things.'.format(sep.join(things)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
