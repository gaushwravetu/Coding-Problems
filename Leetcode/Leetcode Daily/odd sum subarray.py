class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd_count = even_count = 0
        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 0:
                even_count += 1
                result += odd_count
            else:
                odd_count += 1
                result += 1 + even_count
        return result%(10**9+7)
        