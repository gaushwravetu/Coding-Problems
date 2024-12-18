from collections import deque
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Brute Force - O(N^2)
        n = len(prices)
        # for i in range(n):
        #     j = i+1
        #     while(j<n):
        #         if prices[j]<=prices[i]:
        #             prices[i]-=prices[j]
        #             break
        #         j+=1

        # Solving using Monotonic Stack - O(N)
        stack = []
        for i in range(n):
            while(stack and prices[i]<=prices[stack[-1]]):
                top = stack.pop()
                prices[top]-=prices[i]
            stack.append(i)
        return(prices)
                
        