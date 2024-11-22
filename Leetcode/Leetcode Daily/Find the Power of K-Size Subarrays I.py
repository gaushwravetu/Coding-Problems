class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []
        for i in range(n - k + 1):
            sarr = nums[i:i + k]
            if sorted(sarr) == sarr and len(set(sarr)) == k and max(sarr) - min(sarr) == k - 1:
                results.append(max(sarr))
            else:
                results.append(-1)
        
        return results

        