class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 1, max(quantities)
        while left < right:
            mid = (left + right) // 2
            required_stores = sum(math.ceil(q / mid) for q in quantities)
            if required_stores <= n:
                right = mid
            else:
                left = mid + 1
        return left
            