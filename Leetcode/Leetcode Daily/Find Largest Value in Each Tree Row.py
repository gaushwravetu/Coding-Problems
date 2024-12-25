from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        queue = deque([root])
        
        while queue:
            level = len(queue)
            new_max = float('-inf')

            for _ in range(level):

                node = queue.popleft()
                # print(node)
                new_max = max(node.val,new_max)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(new_max)
        
        return result

        