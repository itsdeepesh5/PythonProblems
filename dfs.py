#Traversal

class BT:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None

    def insertLeft(self, val):
        self.left = BT(val)
        #self.left.val=val
        return self.left
    
    def insertRight(self, val):
        self.right = BT(val)
        #self.right.val = val
        return self.right

    def inOrder(self, tree):
        stack= [tree]
        while len(stack):
            node= stack.pop()
            print(node.val)
            if node.left:
                self.inOrder(node.left)
            
            if node.right:
                self.inOrder(node.right)
    def preOrder(self, tree):
        if tree:
            self.preOrder(tree.left)
            print(tree.val)
            self.preOrder(tree.right)

tree= BT(100)
t1=tree.insertLeft(90)
t2= tree.insertRight(150)
t3= t1.insertLeft(80)
t4= t1.insertRight(91)
print(tree.inOrder(tree))
print(tree.preOrder(tree))

