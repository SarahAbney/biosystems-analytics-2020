#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-03-25
Purpose: DNR
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

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    parser.add_argument('-o',
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
    out_dir = args.outdir
    total_seq = 0
    total_files = 0

#    more = 's' if total_files > 1 else ''

    
    for fh in args.file:
        lines = 0
        out_file = os.path.join(out_dir, os.path.basename(fh.name))
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)
        out_fh = open(out_file, 'wt')
    if os.path.isfile(out_file):
        out_file = open(out_file).read().rstrip() 

        more = 's' if total_files > 1 else ''
        total_files = len(os.listdir(out_dir))

 
        for line in fh:
            lines += 1
            rna = ['U' if char == 'T' else char for char in line] 
            listToStr = ''.join(map(str, rna))
            plural = 's' if total_seq > 1 else ''
        total_seq += lines
        plural = 's' if total_seq > 1 else ''


        out_fh.write(listToStr)
        out_fh.close()
    

        
         
    print(f'Done, wrote {total_seq} sequence{plural} in {total_files} file{more} to directory "{out_dir}".')
#    else: 
#        print(f'Done, wrote {total_seq} sequence in {total_files} files to directory "out".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
