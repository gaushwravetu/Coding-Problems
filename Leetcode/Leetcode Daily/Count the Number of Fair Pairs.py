from bisect import bisect_left, bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        flag = 0
        # i,j,flag = 0,n-1,0
        for i in range(n):
            left_flag = lower-nums[i]
            right_flag = upper-nums[i]
            left_flag = bisect_left(nums, left_flag, i + 1)
            right_flag = bisect_right(nums, right_flag, i + 1) - 1
            flag+= max(0,right_flag-left_flag+1)
        return flag


        