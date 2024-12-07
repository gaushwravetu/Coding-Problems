class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        count = 0
        banned = set(banned)
        for i in range(1,n+1):
            if i not in banned:
                maxSum-=i
                # print(maxSum,i)
                if maxSum>=0:
                    count+=1
                if maxSum<0:
                    return count
        return count
        