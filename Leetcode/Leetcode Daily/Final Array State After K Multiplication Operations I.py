import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)
        min_heap = []
        for i in range(n):
            heapq.heappush(min_heap,(nums[i],i))
        while(k>0):
            min_value,index = heapq.heappop(min_heap)
            new_value = min_value*multiplier
            heapq.heappush(min_heap,(new_value,index))
            nums[index]=new_value
            k-=1
        return nums
        