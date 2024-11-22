class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def is_strictly_increasing(start, k):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        
        # Iterate over possible starting points for the first subarray
        for i in range(len(nums) - 2 * k + 1):
            # Check if both subarray `nums[i:i+k]` and `nums[i+k:i+2*k]` are strictly increasing
            if is_strictly_increasing(i, k) and is_strictly_increasing(i + k, k):
                return True
    
        # If no valid pair of adjacent strictly increasing subarrays is found, return False
        return False
        