#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-04-22
Purpose: Win in Vegas
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Take command of the odds"""

    parser = argparse.ArgumentParser(
        description='Counting Cards',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('UserInput',
                        metavar='str',
                        help='Three cards that have been dealt for player(P) and Dealer(D): PPD',
                        default=True)

    parser.add_argument('-d',
                        '--decks',                        
                        help='How many decks do you want to start with?',
                        metavar='int',
                        type=int,
                        default=4)

    parser.add_argument('-b',
                        '--betunit',
                        help='The amount of currency on the betting chip',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-r',
                        '--runningc',
                        help='Running count',
                        metavar='int',
                        type=int,
                        default=0)



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    play = args.UserInput 
    
    cardnum = { '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 0, '8': 0, '9': 0, 'X' : 0, 'J': -1, 'Q': -1, 'K': -1, 'A': -1 } 

    numdecks = args.decks

    count = args.runningc 
    cards = 0 
    totaldecks = 0 

    
    cards += len(play) 
    for card in play: 
        count += cardnum[card.upper()]
        totaldecks = cards / 52
        totalcount = count / (numdecks - totaldecks)
    print(f'Count: {count}')
    print(f'True Count: {totalcount}')
    bet = ((totalcount) - 1)*int(args.betunit) 
        
    print(f'Decks played: {totaldecks}')
    print(f'Raise bet: ${bet}')

# --------------------------------------------------
if __name__ == '__main__':
    main()