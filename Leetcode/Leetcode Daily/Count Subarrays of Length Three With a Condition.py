class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 2):
            first, second, third = nums[i], nums[i + 1], nums[i + 2]
            if first + third == second / 2:
                count += 1
        return count
        