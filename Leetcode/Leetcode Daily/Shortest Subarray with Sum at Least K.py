from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        dq = deque()
        result = float('inf')
        for i in range(n + 1):
            while dq and prefix[i] - prefix[dq[0]] >= k:
                result = min(result, i - dq.popleft())
            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(i)
        return result if result != float('inf') else -1
