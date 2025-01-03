class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        arr_sum = [0]*n
        i = n-1
        mysum,numsum = 0,0
        count = 0
        while(i>=0):
            mysum+=nums[i]
            arr_sum[i]=mysum
            i-=1
        # print(arr_sum)
        for i in range(n-1):
            numsum+=nums[i]
            # print(numsum)
            if numsum>=arr_sum[i+1]:
                count+=1
        return count

        