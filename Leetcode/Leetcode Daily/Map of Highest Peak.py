class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        heights = [[-1] * n for _ in range(m)]  # Initialize heights as -1
        queue = deque()
        
        # Enqueue all water cells and set their heights to 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    queue.append((i, j))
                    heights[i][j] = 0
        
        # Define directions for moving up, down, left, and right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # BFS
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == -1:
                    heights[nx][ny] = heights[x][y] + 1
                    queue.append((nx, ny))
        
        return heights
        