class TreeNode(object):
  def __init__(self, x=None):
    self.data = x	
    self.left = None
    self.right= None


class BinaryTree(object):
  """
  Binary Tree DS with basic functions
  like add a node, deleting a node
  traversal Inorder and postorder
  """

  def __init__(self, x=None):
    self.root = TreeNode(x)
    self.node = None

  def add(self, current, val):
    print("add called", val)
    if not self.root:
      self.root = TreeNode(val)
      return True
    
    #if value is smaller than node 
    if (val == current.data):
      return True
    if (val < current.data):        
      print('1', val, current.data)
      if not current.left:
        current.left = TreeNode(val)
        print('2',current.data)
      else:
        self.add(current.left, val)  
    elif (val > current.data):
      if not current.right:
        print('Right IF',current.data)
        current.right = TreeNode(val)
      else:
        print('Right else',current.data)

        self.add(current.right, val)  
    print('3',current.data)
    return True	  

  def getRoot(self):
    return self.root

  def preorder(self, current):
      if not current:
        return False
      print(current.data,)
      if current.left:
        print("(,")
        self.preorder(current.left)
      if current.right:
        print("),")
        self.preorder(current.right)    

  def inorder(self, current):
      if not current:
        return False
      if current.left:
        self.inorder(current.left)
      print(current.data)
      if current.right:
        self.inorder(current.right)    

if __name__ == "__main__":
  bt= BinaryTree(1)
  root = bt.getRoot()
  for i in range(1,10):
    bt.add(root, i)
  bt.add(root, 12)

  bt.inorder(bt.getRoot())     