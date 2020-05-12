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
    """Bad Cards"""

    
    rv, out = getstatusoutput(f'{prg} AJR')
    assert rv != 0
    assert re.search(f'"AJR" are not valid choices', out)


# --------------------------------------------------
def test_input1_238():
    """input1"""

    expected = ("Count: 2\n"
        "True Count: 0.5073170731707317\n"
        "Decks played: 0.057692307692307696\n"
        "DON'T RISK IT!! Bet differential too low ... $-24.634146341463413")
        
    rv, out = getstatusoutput(f'{prg} 238')
    assert rv == 0
    assert out == expected 


# --------------------------------------------------
def test_input2_2JK():
    """input2"""
    expected = ('Count: -1\n'
        'True Count: -0.25365853658536586\n'
        'Decks played: 0.057692307692307696\n'
        "DON'T RISK IT!! Bet differential too low ... $-62.68292682926829")
    
    rv, out = getstatusoutput(f'{prg} 2JK')
    assert rv == 0 
    assert out == expected

# --------------------------------------------------
def test_input3_runningcflag(): 
    """input3"""
    expected = ('Count: 7.0\n'
        'True Count: 1.7756097560975608\n'
        'Decks played: 0.057692307692307696\n'
        "Raise bet: $38.780487804878035")

    rv, out = getstatusoutput(f'{prg} 23K -r 6')
    assert rv == 0
    assert out == expected

# -------------------------------------------------
def test_input4_runningcflagD():
    """input4"""
    expected = ('Count: 1.5\n'
        'True Count: 0.3804878048780488\n'
        'Decks played: 0.057692307692307696\n'
        "DON'T RISK IT!! Bet differential too low ... $-30.975609756097562")
    
    rv, out = getstatusoutput(f'{prg} 23K -r 0.5')
    assert rv == 0
    assert out == expected 

