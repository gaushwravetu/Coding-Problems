class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k not in nums and max(nums) < k:
            return -1
        nums.sort(reverse=True)
        operations, current_h = 0, max(nums)
        for num in nums:
            if num > k:
                if num != current_h:
                    operations += 1
                    current_h = num
            elif num < k:
                return -1
        if current_h > k:
            operations += 1
        return operations
        