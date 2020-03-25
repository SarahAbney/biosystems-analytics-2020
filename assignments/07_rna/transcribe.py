#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-03-25
Purpose: Transcirbing and Jiving
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Transcribing DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'file',
        metavar='FILE',
        nargs='*',
        type=argparse.FileType('r'),
        help='Input file(s)')

    parser.add_argument(
        '-o',
        '--outdir',
        help='Output directory',
        metavar='DIR',
        type=str,
        default='out')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.file
    out = args.outdir
    total_lines = 0
    
    for fh in dna:
        lines = 0
        out_file = os.path.join(out_dir, os.path.basename(fh.name)
        out_fh = open(out_file, 'wt')
        
        total_files = len(out)

        for line in fh:
            lines += 1
            rna = ['U' if char == 'T' else char for char in dna]

        total_lines += lines

        out_fh.write(rna + '\n')

        print(
            'Done, wrote {total_lines} sequences in {total_files} file into directory "out".'
        )


# --------------------------------------------------
if __name__ == '__main__':
    main()
