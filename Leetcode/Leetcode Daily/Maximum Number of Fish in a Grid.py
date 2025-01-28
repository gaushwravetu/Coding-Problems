class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            fish = grid[x][y]
            grid[x][y] = 0
            
            fish += dfs(x + 1, y)
            fish += dfs(x - 1, y)
            fish += dfs(x, y + 1)
            fish += dfs(x, y - 1)
            
            return fish

        maxFish = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    maxFish = max(maxFish, dfs(i, j))
        
        return maxFish
        