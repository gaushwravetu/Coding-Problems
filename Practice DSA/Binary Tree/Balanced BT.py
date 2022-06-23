class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def checkBalanced(root):
    if root==None:
        return 0

    lh = checkBalanced(root.left)
    rh = checkBalanced(root.right)

    if lh==-1 or rh==-1:
        return -1
    if abs(lh-rh)>1:
        return -1
    return 1+max(lh,rh)

root = Node(1)
root.left = Node(2)
root.left.left = Node(6)
root.left.left.left = Node(7)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

if checkBalanced(root)!=-1:
    print('Balanced')
else:
    print('Unbalanced')