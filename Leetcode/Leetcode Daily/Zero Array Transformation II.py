class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def can_zero_out(k):
            diff = [0] * (n + 1)
            temp_nums = nums[:]
            for i in range(k):
                l, r, val = queries[i]
                diff[l] -= val
                if r + 1 < n:
                    diff[r + 1] += val
            current_decrement = 0
            for i in range(n):
                current_decrement += diff[i]
                temp_nums[i] += current_decrement
                if temp_nums[i] > 0:
                    return False
            return True
        left, right = 0, len(queries)
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if can_zero_out(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result