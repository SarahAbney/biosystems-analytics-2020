#!/usr/bin/env python3
"""tests for casinocounter.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './casinocounter.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_string():
    """Bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"invalid choice: '{bad}'", out)


# --------------------------------------------------
def test_input1_238():
    """input1"""
    expected = '\n'.join([
        'Count: 2', 'True Count: 0.5073170731707317',
        'Decks played: 0.057692307692307696',
        'Raise bet: $-24.634146341463413',
        'Player, what cards have been dealt? [q to quit]: '
    ])

    #run('238', expected, 0)
    rv, out = getstatusoutput(f'{prg} JQK')
    assert rv != 0
    assert out == expected


# --------------------------------------------------
def test_input2_2JK():
    """input2"""
    expected = '\n'.join([
        'Count: -1', 'True Count: -0.25365853658536586',
        'Decks played: 0.057692307692307696',
        "DON'T RISK IT!! Bet differential too low ... $-62.68292682926829",
        'Player, what cards have been dealt? [q to quit]: '
    ])

    run('2JK', expected, 0)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
