class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key



def checkBT(R1,R2):
    if R1==None and R2==None:
        return True
    if R1 is not None and R2 is not None:
        return (R1.val==R2.val and checkBT(R1.left,R2.left) and checkBT(R1.right,R2.right))

    return False
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)

print(checkBT(root,root2))
