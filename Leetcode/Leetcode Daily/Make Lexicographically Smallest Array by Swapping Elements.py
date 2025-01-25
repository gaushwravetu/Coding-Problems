from typing import List
from collections import defaultdict, deque
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        groups = defaultdict(deque)
        element_to_group = {}
        group_id = 0
        groups[group_id].append(sorted_nums[0])
        element_to_group[sorted_nums[0]] = group_id
        
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] - groups[group_id][-1] <= limit:
                groups[group_id].append(sorted_nums[i])
            else:
                group_id += 1
                groups[group_id].append(sorted_nums[i])
            element_to_group[sorted_nums[i]] = group_id
        
        for i in range(len(nums)):
            group_id = element_to_group[nums[i]]
            nums[i] = groups[group_id].popleft()
        
        return nums
        