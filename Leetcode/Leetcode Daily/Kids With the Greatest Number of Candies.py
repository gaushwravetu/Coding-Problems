class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        resultmax = max(candies)
        result = []
        n = len(candies)
        for i in range(0,n):
            if candies[i]+extraCandies>=resultmax:
                candies[i]=True
            else:
                candies[i]=False
        return candies

        