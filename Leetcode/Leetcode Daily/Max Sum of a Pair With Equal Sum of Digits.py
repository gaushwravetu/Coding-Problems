from collections import defaultdict
from sortedcontainers import SortedList
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sumdict = defaultdict(SortedList)
        n = len(nums)
        result = -1
        def value(x):
            return sum(map(int, str(x)))

        for i in range(n):
            sumdict[value(nums[i])].add(nums[i])

        # print(sumdict)

        for i in sumdict:
            if len(sumdict[i])>1:
                result = max(result,sumdict[i][-1]+sumdict[i][-2])

        return result
        