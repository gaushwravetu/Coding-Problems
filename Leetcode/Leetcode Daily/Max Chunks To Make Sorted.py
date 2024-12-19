class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_chunk = 0
        count = 0
        n = len(arr)
        for i in range(n):
            max_chunk = max(max_chunk,arr[i])
            if max_chunk == i:
                count+=1
        return count
        