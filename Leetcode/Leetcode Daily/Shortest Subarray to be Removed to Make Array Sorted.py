from bisect import bisect_left
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l_side = 0
        while l_side < n - 1 and arr[l_side] <= arr[l_side + 1]:
            l_side += 1
        if l_side == n - 1:
            return 0
        r_side = n - 1
        while r_side > 0 and arr[r_side - 1] <= arr[r_side]:
            r_side -= 1
        flag_arr = min(n - l_side - 1, r_side)
        for i in range(l_side + 1):
            j = bisect_left(arr, arr[i], r_side, n)
            if j < n:
                flag_arr = min(flag_arr, j - i - 1)
        return flag_arr
        