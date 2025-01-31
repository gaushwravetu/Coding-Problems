class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        island_id = 2
        island_sizes = {0: 0}
        
        def dfs(r, c, island_id):
            stack = [(r, c)]
            size = 0
            while stack:
                i, j = stack.pop()
                if 0 <= i < n and 0 <= j < n and grid[i][j] == 1:
                    grid[i][j] = island_id  # Mark with island ID
                    size += 1
                    stack.extend([(i-1, j), (i+1, j), (i, j-1), (i, j+1)])
            return size
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1
        max_size = max(island_sizes.values(), default=0)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    unique_neighbors = set()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            unique_neighbors.add(grid[nr][nc])
                    
                    new_size = 1 + sum(island_sizes[i] for i in unique_neighbors)
                    max_size = max(max_size, new_size)

        return max_size
        