class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incr_len,decr_len = 1,1
        max_len = 1
        n = len(nums)
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                incr_len+=1
                decr_len = 1
            elif nums[i]>nums[i+1]:
                decr_len+=1
                incr_len = 1
            else:
                decr_len,incr_len = 1,1
            
            max_len = max(max_len,incr_len,decr_len)

        return max_len
        