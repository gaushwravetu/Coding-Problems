class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        valid_count = 0
        for start in range(n):
           if nums[start] == 0:
               temp_nums = nums[:]
               test = start
               flag = -1
               while 0 <= test < n:
                   if temp_nums[test] > 0:
                       temp_nums[test] -= 1
                       flag = -flag
                   test += flag
               if all(x == 0 for x in temp_nums):
                   valid_count += 1
               temp_nums = nums[:]
               test = start
               flag = 1
               while 0 <= test < n:
                   if temp_nums[test] > 0:
                       temp_nums[test] -= 1
                       flag = -flag
                   test += flag
               if all(x == 0 for x in temp_nums):
                   valid_count += 1
        return valid_count