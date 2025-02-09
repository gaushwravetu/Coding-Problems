from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        good_pairs = 0
        n = len(nums)

        for i, num in enumerate(nums):
            key = i - num
            good_pairs += freq[key]  # Count pairs with same key
            freq[key] += 1

        total_pairs = n * (n - 1) // 2
        return total_pairs - good_pairs
        