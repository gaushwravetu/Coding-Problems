import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # I want to implement max heap by negating the elements, since only support min heap
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        total_gifts = sum(gifts)
        for i in range(k):
            max_gift = -heapq.heappop(max_heap)
            new_gift = math.floor(math.sqrt(max_gift))
            
            total_gifts-=max_gift
            total_gifts+=new_gift

            heapq.heappush(max_heap,-new_gift)
            # print(max_heap)
        
        # print(total_gifts)
        return total_gifts