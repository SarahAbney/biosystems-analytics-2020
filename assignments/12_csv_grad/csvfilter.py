#!/usr/bin/env python3
"""
Author : seabney
Date   : 2020-05-07
Purpose: CSV Filter
"""

import argparse
import os
import sys
import csv
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='CSV Filter',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None,
                        required=True,
                        help='Input file')

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        required=True,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filname',
                        metavar='OUTFILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        metavar='delimiter',
                        help='Input delimiter',
                        default=',')

    args = parser.parse_args()


    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    column = args.col 
    search_for = args.val
   # infile = args.file

     

     
    read = csv.DictReader(args.file, delimiter=args.delimiter) 
    writer = csv.DictWriter(args.outfile, fieldnames=read.fieldnames)
    writer.writeheader()
    linecount = 0
    headers = ','.join(read.fieldnames)

    if re.search(column, headers, re.IGNORECASE):
    
        for line in read:
            if column and search_for: 
                text = line[column] 
                if re.search(column, str(line.keys()), re.IGNORECASE):        
                    if re.search(search_for, text, re.IGNORECASE): 
                        writer.writerow(line)
                        linecount += 1

            elif search_for: 
                if re.search(search_for, str(line.values()), re.IGNORECASE):
                    writer.writerow(line) 
                    linecount += 1
    else:
        sys.exit(f'--col "{args.col}" not a valid column!')

          




        
        
       # if column in range(len(line.keys())):
            # re.search(str(column), str(line.keys()), re.IGNORECASE)
       # for search_for in range(len(line.values())):
           # if re.search(str(search_for), str(line.values()), re.IGNORECASE):
                
       # if column in range(len(infile.readline())):
           ## if re.search(str(column), str(line.keys()), re.IGNORECASE):
           
       ##  writer.writerow(line)
           # for search_for in range(len(line.values())):                                       # if re.search(str(search_for), str(line.values()), re.IGNORECASE): 


           # if re.search(str(column), str(read.fieldnames), re.IGNORECASE):
           # for search_for in range(len(line.values())):
             ##   if re.search(str(search_for), str(line.values()), re.IGNORECASE):                   writer.writerow(line) 
            
   # for fh in infile: 

       # if re.search(column, ','.join(read.fieldnames), re.IGNORECASE):
        #    for line in read:
         #       headers = csv.DictWriter(args.outfile, line) 

          #      if column in line:
           #         if re.search(column, str(headers), re.IGNORECASE):
            #            if re.search(val, line, re.IGNORECASE):
                   # if val.lower() in line:    
             #               writer.writerows(line)
       
              #  elif val.lower() in line:
               #     if re.search(val, line, re.IGNORECASE): 
                #        writer.writerow(line)
        
              #  elif column in line: 
               #     if val.lower() in line: 
               # if re.search(val, str(line.values()), re.IGNORECASE):
               # if re.search(column, headers, re.IGNORECASE):
                #        writer.writerows(line)
       # else: 
        #    sys.exit(f'--col "{args.col}" not a valid column!')
                
        
    print(f'Done, wrote {linecount} to "{args.outfile.name}".')

#  ---------------------------------------------------
if __name__ == '__main__':
    main()
