class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = max_ans = 0
        for num in nums:
            max_sum = max(num, max_sum + num)
            min_sum = min(num, min_sum + num)
            max_ans = max(max_ans, abs(max_sum), abs(min_sum))
        return max_ans
        