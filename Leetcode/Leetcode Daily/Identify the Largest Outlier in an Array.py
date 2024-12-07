from itertools import combinations
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_outlier = None
        for comb in combinations(nums, n - 2):
            special_sum = sum(comb)
            remaining = nums.copy()
            for num in comb:
                remaining.remove(num)
            if special_sum in remaining:
                remaining.remove(special_sum)
                if remaining:
                    max_outlier = max(max_outlier if max_outlier is not None else float('-inf'), remaining[0])
        return max_outlier
        
        