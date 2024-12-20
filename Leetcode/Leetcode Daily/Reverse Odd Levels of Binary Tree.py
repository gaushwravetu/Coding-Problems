# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # BFS queue to traverse level by level
        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            level_nodes = []  # Store nodes at the current level

            # Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                if level % 2 == 1:
                    level_nodes.append(node)  # Store nodes for reversal
                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Reverse the values of the current odd level nodes
            if level % 2 == 1:
                values = [node.val for node in level_nodes]
                values.reverse()
                for i, node in enumerate(level_nodes):
                    node.val = values[i]

            level += 1

        return root
        
        