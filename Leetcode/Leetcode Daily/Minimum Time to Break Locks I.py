from typing import List
from itertools import permutations
class Solution:
    def findMinimumTime(self, strength: List[int], K: int) -> int:
        res = -1
        for ss in permutations(strength):
            x = 1
            cur = 0
            for s in ss:
                cur += (s + x - 1) // x  # Time to break the current lock
                x += K  # Update the factor X after breaking the lock
            if res == -1 or cur < res:
                res = cur  # Update minimum time
        return res

        