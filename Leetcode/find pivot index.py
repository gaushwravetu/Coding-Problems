class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left,right = 0,sum(nums)
        n = len(nums)
        for i in range(n):
            right-=nums[i]
            if right==left:
                return i
            left+=nums[i]
        return -1

# print(~~~2017+1)