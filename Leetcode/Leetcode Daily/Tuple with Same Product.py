class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                count += 8 * product_map[product]
                product_map[product] += 1

        return count
        