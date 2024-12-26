class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if (target + total_sum) % 2 != 0 or total_sum < abs(target):
            return 0

        subset_sum = (target + total_sum) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # 1 way to make sum 0
        
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset_sum]
        