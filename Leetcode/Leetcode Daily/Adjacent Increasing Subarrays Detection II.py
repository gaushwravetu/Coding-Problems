class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Precompute incr_length array
        incr_length = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                incr_length[i] = incr_length[i + 1] + 1
    
        # Step 2: Binary search for the maximum k
        left, right = 1, n // 2
        result = 0
    
        while left <= right:
            mid = (left + right) // 2
            found = False
            # Check if there exists an i such that both incr_length[i] and incr_length[i + mid] >= mid
            for i in range(n - 2 * mid + 1):
                if incr_length[i] >= mid and incr_length[i + mid] >= mid:
                    found = True
                    break
            if found:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
    
        return result