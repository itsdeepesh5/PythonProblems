#!/usr/bin/python 2.4

import os
import re
import sys

def listdir(path):
  for i in os.listdir(path):
    match= re.search(r'\w+.py',i)
    if match:
      print(match.group())

def main():
  listdir(sys.argv[1])

if __name__ == '__main__':
  main()