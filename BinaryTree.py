class BinaryTreeNode(object):
    def __init__(self, value):
        self.left=None
        self.right=None
        self.value= value

    def insert_left(self, value):
        self.left= BinaryTreeNode(value)
        return self.left
    def insert_right(self, value):
        self.right= BinaryTreeNode(value)
        return self.right


def dfs(root):
    if root is None:
        return None
    stack= []
    stack.append(root)
    while len(stack) > 0:
        current= stack.pop()
        print(current.value,)
        #Leaf Node
        if current.left is None and current.right is None:
            print('Touched Leaf', current.value)

        else:
            if current.right:
                stack.append(current.right)
            if current.left:
                print(current.left.value)
                stack.append(current.left)

        
        


tree= BinaryTreeNode(10)
left = tree.insert_left(20)
right = tree.insert_right(15)
ll= left.insert_left(9)
ll= left.insert_right(8)



print(dfs(tree))


    
