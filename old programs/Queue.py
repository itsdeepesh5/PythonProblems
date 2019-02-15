#!/usr/python 

import sys

#Front is for alternate implementation
class Queue:

  def __init__(self, value=None):
    self.front=self.rear=0
    self.data=[]
    self.size= 0
    if value:
      self.data.append(value)
      self.size=1

  def isempty(self):
    return not self.data
       
  def enqueue(self, value):    
    if value:
      self.data.append(value)
      self.rear+=1
      self.size+=1
      print('Current Status Enqueue', self.front, self.rear) 
    return True

  def dequeue(self):
    if self.isempty():
      return None
    
    if(self.front < self.rear):
      ret = self.data[self.front]
      print('Current Status Enqueue', self.front, self.rear)       
      del self.data[self.front]
      #self.front+=1
      self.size-=1
      return ret  
    return None

  def viewQueue(self):
    if self.isempty():
      return None
    return self.data 

  def getSize(self):
    return self.size

def main():
  queue= Queue(5)
  print(queue.viewQueue())    
  for i in range(10):
    queue.enqueue(i)
  print(queue.viewQueue())    

  while not queue.isempty():
    print(queue.dequeue())
  print(queue.viewQueue())
if __name__ == '__main__':
  main()     
    
