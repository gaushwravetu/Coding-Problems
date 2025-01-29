class Solution:    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [1] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])  # Path compression
                return self.parent[x]

            def union(self, x, y):
                rootX, rootY = self.find(x), self.find(y)
                if rootX == rootY:
                    return False  # Cycle detected
                if self.rank[rootX] > self.rank[rootY]:
                    self.parent[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.parent[rootX] = rootY
                else:
                    self.parent[rootY] = rootX
                    self.rank[rootX] += 1
                return True
                
        dsu = DSU(len(edges) + 1)
        for u, v in edges:
            if not dsu.union(u - 1, v - 1):  # Nodes are 1-based, adjust to 0-based
                return [u, v]
        