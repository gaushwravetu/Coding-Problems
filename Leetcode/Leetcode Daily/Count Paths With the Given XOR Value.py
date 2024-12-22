class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
    
        @lru_cache(None)
        def dp(i, j, xor_val):
            if i >= m or j >= n:
                return 0
    
            xor_val ^= grid[i][j]
    
            if i == m - 1 and j == n - 1:
                return 1 if xor_val == k else 0
    
            right_paths = dp(i, j + 1, xor_val)
            down_paths = dp(i + 1, j, xor_val)
    
            return (right_paths + down_paths) % MOD
    
        return dp(0, 0, 0)
        