class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = max(nums)
        n = len(nums)
        mysum = 0
        for i in range(n):
            mysum+=nums[i]
            if mysum<0:
                mysum = 0
            result = max(result,mysum)
        if result==0:
            return max(nums)
        return result