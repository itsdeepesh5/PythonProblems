#!/usr/bin/python 2.4

import os
import re
import sys

def longestword(string):
    #match= re.search(r'[\d.+\w+\d+]',string)
    match = re.split('[^\d+\w+]', string)
    if match:
      print(sorted(match, key=len, reverse=True)[0])

def main():
  longestword(sys.argv[1])

if __name__ == '__main__':
  main()