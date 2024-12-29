class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])
        
        freq = [[0] * n for _ in range(26)]
        for word in words:
            for j, char in enumerate(word):
                freq[ord(char) - ord('a')][j] += 1
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        
       
        for i in range(m + 1):  
            for j in range(1, n + 1):  
                dp[i][j] = dp[i][j - 1]  
                
                if i > 0: 
                    char_idx = ord(target[i - 1]) - ord('a')
                    dp[i][j] += dp[i - 1][j - 1] * freq[char_idx][j - 1]
                    dp[i][j] %= MOD 
        
        return dp[m][n]
        