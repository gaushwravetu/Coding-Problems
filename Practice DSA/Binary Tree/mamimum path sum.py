class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
def maxpathsum(root,maxi):

    if root==None:
        return 0
    lh = (maxpathsum(root.left,maxi))
    rh = (maxpathsum(root.right,maxi))

    maxi = max(maxi,lh+rh+root.val)
    result = max(lh+rh)+root.val
    return result

root = Node(-10)
root.left = Node(7)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(11)
maxi = 0
print(maxpathsum(root,maxi))