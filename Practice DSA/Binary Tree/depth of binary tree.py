from turtle import right


class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def printMaxDepth(root):
    if root == None:
        return 0
    left = (printMaxDepth(root.left))
    right =(printMaxDepth(root.right))
    result = 1+max(left,right)
    return result



root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)

print(printMaxDepth(root))