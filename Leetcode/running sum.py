class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # nums = list(map(int,input().split()))
        nsum = 0
        outnum = []
        for i in nums:
            nsum+=i
            outnum.append(nsum)
        return(outnum)

    