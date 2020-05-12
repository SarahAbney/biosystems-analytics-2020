#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-04-22
Purpose: Learn how to count
"""

import argparse
import os
import sys
import re


# --------------------------------------------------
def get_args():
    """Take command of the odds"""

    parser = argparse.ArgumentParser(
        description='Counting Cards',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('user_input',
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
                        metavar='float',
                        type=float,
                        default=0)

    args = parser.parse_args()

    if not re.match('[2-9XJQKA]{3}', args.user_input):
        parser.error(f'Bad input: Stop! Are you even playing cards? "{args.user_input}" are not valid choices. Choose from "2,3,4,5,6,7,8,9,X,J,Q,K,A".')

    return args


# --------------------------------------------------
#def main():
def main() -> None: 
    """Make a jazz noise here""" 
    args = get_args()
    play = args.user_input
    numdecks = args.decks
    count = args. runningc
    cards = 0
    totaldeck = 0
    
    
    cardnum = { '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 0, '8': 0, '9': 0, 'X' : 0, 'J': -1, 'Q': -1, 'K': -1, 'A': -1 } 
     
    cards += len(play)
    for card in play: 
        count += cardnum[card.upper()]
        totaldecks = cards / 52
        totalcount = count / (numdecks - totaldecks)
    
    print(f'Count: {count}')
    print(f'True Count: {totalcount}')



    bet = ((totalcount) - 1)*int(args.betunit) 

    print(f'Decks played: {totaldecks}') 

    if bet < 1: 
        print(f"DON'T RISK IT!! Bet differential too low ... ${bet}")
    else: 
        print(f'Raise bet: ${bet}')

    
# --------------------------------------------------
if __name__ == '__main__':
    main()
