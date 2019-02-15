#!/usr/python 

import sys

def createDic(filename):
  print('Hello')
  f= open(filename,'rU')
  text=f.read()
  d={}
  for i in text.lower().split():
    if i in d:
      d[i]=d.get(i) + 1
    else:
      d[i]=1	
  return d

def returnKey(i):
  return d[i]

def pickCount(filename, opt):
  d= createDic(filename)
  if opt=='count':
    d.items()
  else:
    return sorted(d, key=d.__getitem__, reverse=True)

if __name__ == '__main__':
  print(pickCount(sys.argv[1], sys.argv[2]))	