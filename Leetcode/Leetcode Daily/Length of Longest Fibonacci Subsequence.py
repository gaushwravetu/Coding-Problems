class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        dp = defaultdict(lambda: 2)
        max_length = 0

        for j in range(len(arr)):
            for i in range(j):
                x = arr[j] - arr[i]
                if x < arr[i] and x in index:
                    k = index[x]
                    dp[i, j] = dp[k, i] + 1
                    max_length = max(max_length, dp[i, j])

        return max_length if max_length > 2 else 0
        