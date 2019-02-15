class LNode(object):
  def __init__(self, value=None):
    self.value = value
    self.next=None
  
class LinkedList(object):
  def __init__(self, value=None):
    self.root = LNode(value)
    self.root.next=None

  def addNode(self, value=None):
    if self.root:
      newNode= LNode(value)
      newNode.next = self.root.next
      self.root.next = newNode
    else:
      newNode= LNode(value)
      newNode.next =None
    return True
	      
  def isempty(self):
    if self.root:
      return False
    return True 
  
  def printList(self):
    current= self.root
    while(current):
      print(current.value,'-->')
      current= current.next


  # root -> 1-2-3-4-5 - NULL
  #

  def reverseUsingRec(self):
    self.reverseUsingRecursion(self.root)


  def reverseUsingRecursion(self, current):
    if not current:
      return None
    if not current.next:
      self.root = current
      #self.next = None
      return current
    next = current.next
    current.next = None
    rest = self.reverseUsingRecursion(next)
    next.next = current
    #current.next.next = current
    #print(next.value)
    current.next = None	    
    return rest

    #while(current):
    #  next = current.next

    #  current.next = prev   
    #  prev=current
    #  current= next
    #self.root = prev
	

  def reverse(self):
    current= self.root
    prev= None
    
    while(current):
      next = current.next

      current.next = prev   
      prev=current
      current= next
    self.root = prev
    
  def removeNode(self, target):
    if self.isempty():
      return False
    current=self.root
    prev = None
    while current:
      if current.value == target:
        if prev:
          prev.next  = current.next
	else:
          self.root = current.next   		
        return True
      prev = current		
      current= current.next	
    return False

if __name__ == "__main__":
  lnode= LNode(45)
  linkedNode = LinkedList(1)
  for i in range(1,10):    
    linkedNode.addNode(i)
  linkedNode.printList()
  print("Elements Added")

  
  linkedNode.printList()
  for i in range(6,10):
    print(linkedNode.removeNode(i))
  linkedNode.printList()

  print('REverse Started')
  linkedNode.reverseUsingRec()
  print('REverse Done')
  linkedNode.printList()

