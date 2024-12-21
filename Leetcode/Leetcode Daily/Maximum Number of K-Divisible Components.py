from collections import defaultdict
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        def dfs(node, parent):
            nonlocal removable_edges
            total = nums[node]
            for neighbor in tree[node]:
                if neighbor != parent:
                    total += dfs(neighbor, node)
            if total % k == 0:
                removable_edges += 1
                return 0
            return total
        
        removable_edges = 0
        dfs(0, -1)
        return removable_edges
        