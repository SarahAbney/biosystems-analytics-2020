#!/usr/bin/env python3
""" Author: Sarah Abney 
    Purpose: Homework 1 """



import argparse 
import sys 
import os 


# --------------------------------------------------
def get_args():


            parser = argparse.ArgumentParser(
                 description="Find positon of vowel in string",
                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
            
            parser.add_argument('vowel',
                    metavar = 'vowel', 
                    type=str,
                    help='vowel = A vowel to search for')

            parser.add_argument('text',  
                    metavar='word',
                    type=str,
                    help= 'text = The text to show')
            
            return parser.parse_args() 

#-----------------------------------------

def main(): 

    args = get_args()
    text = args.text 
    vowel = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
    index = vowel.index('a','e','i')
          = vowel.index('o', 'u', 'A')
          = vowel.index('E', 'I', 'O')
          = vowel.index('U')

    print(f'Found "{vowel}" in "{text}" at index {index}') if text in 'aeiou' else print (f'"{vowel}" is not found in "{text}"') 
#--------------------------------------------
if __name__=='__main__':
    main()

