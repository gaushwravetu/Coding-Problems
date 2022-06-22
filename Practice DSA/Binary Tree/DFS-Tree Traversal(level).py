class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def printLevel(root):
    if root==None:
        return
    queue = []
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].val)
        node = queue.pop(0)
        if node.left!=None:
            queue.append(node.left)
        if node.right!=None:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(printLevel(root))