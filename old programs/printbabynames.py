#!/usr/bin/python

import re
import sys

def findYear(filename):
  f= open(filename, 'r')
  match =re.search('(Popular Names in )(\d\d\d\d)', f.read())
  return(match.group(2))


def findbabyNames(filename):
  f= open(filename, 'r')
  match=re.findall(r'(<td>)(\d)(</td> <td>)(\w+)(</td> <td>)(\w+)(</td>)', f.read())
  l=[]
  for i in match:
    l.append([i[3],i[1]])
    l.append([i[5],i[1]])
  return sorted(l)
  
if __name__ == '__main__':
  try:
    names=findbabyNames(sys.argv[1])
    f= open(sys.argv[1]+'.summary','w')
    f.write(findYear(sys.argv[1])+'\n'+  '\n'.join([i[0]+' '+i[1] for i in names]))
    f.close()
  except Exception as e:
    print "No files found"
    raise e
