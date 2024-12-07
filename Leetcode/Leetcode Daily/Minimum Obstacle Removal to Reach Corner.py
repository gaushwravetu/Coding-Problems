import heapq
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
   
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        
        # Priority queue for Dijkstra's algorithm
        pq = [(0, 0, 0)]  # (obstacles_removed, row, col)

        while pq:
            obstacles, row, col = heapq.heappop(pq)

            # If we reach the bottom-right corner
            if row == m - 1 and col == n - 1:
                return obstacles

            # Mark as visited
            if visited[row][col]:
                continue
            visited[row][col] = True

            # Explore neighbors
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                    heapq.heappush(pq, (obstacles + grid[r][c], r, c))

        return -1  # Shouldn't reach here

        
        