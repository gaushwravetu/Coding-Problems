import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        min_heap = []
        # bulding the min heap to store smallest elements based on their indices
        for i in range(n):
            heapq.heappush(min_heap,(nums[i],i))
        # Taking set to track the visited indices
        visited = set()
        result = 0
        while(len(visited)<n):
            while min_heap:
                element,index = heapq.heappop(min_heap)
                if index not in visited:
                    break
            visited.add(index)
            if index-1>=0:
                visited.add(index-1)
            if index+1<n:
                visited.add(index+1)
            result+=element
        return result
                