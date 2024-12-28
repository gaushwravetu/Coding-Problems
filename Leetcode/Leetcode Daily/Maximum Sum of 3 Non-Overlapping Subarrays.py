class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: Compute the sum of all subarrays of length k
        window_sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        window_sums[0] = current_sum
        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            window_sums[i] = current_sum

        # Step 2: Compute left and right arrays
        left = [0] * len(window_sums)
        best_left = 0
        for i in range(len(window_sums)):
            if window_sums[i] > window_sums[best_left]:
                best_left = i
            left[i] = best_left

        right = [0] * len(window_sums)
        best_right = len(window_sums) - 1
        for i in range(len(window_sums) - 1, -1, -1):
            if window_sums[i] >= window_sums[best_right]:
                best_right = i
            right[i] = best_right

        # Step 3: Find the best middle subarray
        max_sum = 0
        result = []
        for j in range(k, len(window_sums) - k):
            left_idx = left[j - k]
            right_idx = right[j + k]
            total = window_sums[left_idx] + window_sums[j] + window_sums[right_idx]
            if total > max_sum:
                max_sum = total
                result = [left_idx, j, right_idx]

        return result
        