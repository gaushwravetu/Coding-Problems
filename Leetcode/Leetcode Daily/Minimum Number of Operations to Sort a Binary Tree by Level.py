# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        levels = self.levelOrderTraversal(root)
        total_swaps = 0
        
        # Processing each level to count swaps
        for level in levels:
            total_swaps += self.countMinSwaps(level)
        
        return total_swaps

    def levelOrderTraversal(self, root):
        # Performing a level order traversal and storing each level's values
        levels = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            levels.append(level)
        
        return levels

    def countMinSwaps(self, arr):
        # finging the number of swaps required to sort the array
        n = len(arr)
        sorted_arr = sorted(arr)
        index_map = {value: i for i, value in enumerate(sorted_arr)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i] == sorted_arr[i]:
                continue
            
            # checking for the cycle
            cycle_size = 0
            x = i
            while not visited[x]:
                visited[x] = True
                x = index_map[arr[x]]
                cycle_size += 1
            
            # If the cycle size is greater than 1, add (cycle_size - 1) to swaps
            if cycle_size > 1:
                swaps += (cycle_size - 1)
        
        return swaps
        