#\usr/bin\python2

import sys

class Stack:
  def __init__(self, value=None):
    self.data=[]
    self.index=0
    if value:
      self.data.append(value)
      self.index+=1

  def pop(self):
    self.index-= 1 
    return self.data.pop()
  
  def push(self, value):
    if value:
      self.data.append(value)
      self.index+= 1
      return True	
    return False

  def displayStack(self):
    return (self.data)
	
def main():
  print("Creating Index")
  l = Stack(4)
  l.push(5)
  l.push(6)
  print(l.displayStack())
  print(l.pop())
  print(l.pop())

if __name__ == '__main__':
  main()