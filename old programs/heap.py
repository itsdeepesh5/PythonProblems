
class Heap(object):
  """ Heap will use function max extract, Heapify, max(), add, delete etc.
 	Head Sort

  """

  def __init__(self, x):
    self.list=[0]
    for i in x:
      self.add(i)

  def getMax(self):
    if len(self.list) > 1:
      return self.list[1]
    return None

  def pop(self):
    #  Swap with the max
    if not self.list:
      return None	
    max = self.getMax()
    self.list[1], self.list[len(self.list)-1] = self.list[len(self.list)-1] , self.list[1]
    #  Pull max and delete it
    print('Del', self.list[len(self.list)-1])
    del self.list[len(self.list)-1]
    #  Heapify or bubble down index 1     
    if self.list > 1:
      self.heapify(1)
    return max
    		  
  #Bubble Down
  def heapify(self, p):
    while p < (len(self.list)/2):
      left = 2*p 
      right = 2*p + 1
      print('Heapify', left, right)
      if left < len(self.list) and (self.list[p] < self.list[left]): 
        (self.list[p] ,  self.list[left]) = (self.list[left] , self.list[p])
      
      if right < len(self.list) and self.list[p] < self.list[right]: 
        (self.list[p] ,  self.list[right]) = (self.list[right] , self.list[p])

      p+=1	
      #self.heapify(self, p)

  def heapifySort(self, list,  p):
    while p < (len(list)/2):
      left = 2*p 
      right = 2*p + 1
      print('Heapify Sort', left, right, list)
      if left < len(list) and (list[p] < list[left]): 
        (list[p] ,  list[left]) = (list[left] , list[p])
      
      if right < len(list) and list[p] < list[right]: 
        (list[p] ,  list[right]) = (list[right] , list[p])

      p+=1	
  

  def heapifyUp(self, p):
    if p ==1:
      return True
    while p > 1 :
      parent = p//2 
      print('Heapify Up', parent, self.list)
      if parent > 0 and (self.list[parent] < self.list[p]): 
        (self.list[p] ,  self.list[parent]) = (self.list[parent] , self.list[p])
        p = parent


  def add(self, val):
    self.list.append(val)
    self.heapifyUp(len(self.list)-1)
    print('add', self.list)
    return True	
  def printHeap(self):
    print(self.list[1:])
  
  
  def heapSort(self):
    for i in xrange(len(self.list)-1, 1,-1):
      self.list[i], self.list[1] = self.list[1], self.list[i]
      self.heapifySort(self.list[:i], 1)
    self.printHeap()        


	
if __name__ == "__main__":
  s = Heap([])
  for i in xrange(10,23):
    s.add(i)     
  print(s.getMax())
  print('POP',s.pop())    
  print(s.getMax())
  s.printHeap()  
  s.heapSort()
  print('After Sorting')
  s.printHeap()  
	