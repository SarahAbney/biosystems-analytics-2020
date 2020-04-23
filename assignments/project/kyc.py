#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-04-22
Purpose: Win in Vegas
"""

import argparse
import os
import re
import sys
from typing import List, NamedTuple, Optional


class State(NamedTuple):
    player: str = 'Babbit'
    runningcount: int = 0
    quit: bool = False
    error: Optional[str] = None
    winner: Optional[str] = None


# --------------------------------------------------
def get_args():
    """Take command of the odds"""

    parser = argparse.ArgumentParser(
        description='Counting Cards',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'UserInput',
        metavar='str',
        help=
        'Three cards that have been dealt for player(P) and Dealer(D): PPD',
        default=True,
    )
        # choices=[
        #     '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K', 'A'
        # ])

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

    args = parser.parse_args()

    if not re.match('[2-9XJQKA]{3}', args.UserInput):
        parser.error(f'Bad input "{args.UserInput}"')

    return args


# --------------------------------------------------
#def main():
def main() -> None:
    """Make a jazz noise here"""
    state = State()
    args = get_args()
    play = args.UserInput

    cardnum = {
        '2': 1,
        '3': 1,
        '4': 1,
        '5': 1,
        '6': 1,
        '7': 0,
        '8': 0,
        '9': 0,
        'X': 0,
        'J': -1,
        'Q': -1,
        'K': -1,
        'A': -1
    }

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
    bet = ((totalcount) - 1) * int(args.betunit)

    print(f'Decks played: {totaldecks}')

    if bet < 1:
        print(f"DON'T RISK IT!! Bet differential too low ... ${bet}")
    else:
        print(f'Raise bet: ${bet}')

#added to append running count
    while True:
        print((state.count))

        if state.error:
            print(state.error)

        state = get_move(state)

        if state.quit:
            print('BOO! "100% of shots not taken are missed"!!!')
            break
        elif state.winner:
            print(f'Back out and Cash out!')
            break


# --------------------------------------------------
def get_move(state: State) -> State:
    "get the dealt cards"

    player = state.player
    cell = input(f'Player, what cards have been dealt? [q to quit]: ')
    if cell == 'q':
        return state._replace(quit=True)

    runningcount = state.totalcount


# -------------------------------------------------
def find_winner(totalcount: List[str]) -> Optional[str]:
    'Cash out!!'

    winning = (bet) > 1000

    return None


# --------------------------------------------------
if __name__ == '__main__':
    main()
