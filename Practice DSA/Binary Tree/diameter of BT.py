class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def diameterBT(diameter,root):
    if root==None:
        return 0
    lh = diameterBT(diameter,root.left)
    rh = diameterBT(diameter,root.right)

    diameter = max(diameter,lh+rh)
    print(diameter)

    return 1+lh+rh

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(6)
# root.left.left.left = Node(7)
# root.left.left.right = Node(8)
diameter = 0

print(diameterBT(diameter,root))
