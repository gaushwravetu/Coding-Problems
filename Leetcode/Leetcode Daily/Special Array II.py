class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Brute Force Technique
        # Time complexity - O(n*m)
        m = len(queries)
        n = len(nums)
        # flag_nums = [False]*(n-1)
        flag_queries = [False]*(m)
        # for i in range(n-1):
        #     if abs(nums[i]-nums[i+1])%2!=0:
        #         flag_nums[i]=True
        # for j in range(m):
        #     if not all(flag_nums[queries[j][0]:queries[j][1]]):
        #         flag_queries[j]=False
        #     else:
        #         flag_queries[j]=True
        # # print(flag_nums)
        # return flag_queries

        # Lets implement the cummlative sum approach
        cumlative_sum = [0]*n
        count = 0
        for i in range(n-1):
            if abs(nums[i]-nums[i+1])%2==0:
                count+=1
                cumlative_sum[i+1]=count
            cumlative_sum[i+1] = count
        # print(cumlative_sum)
        for j in range(m):
            if (cumlative_sum[queries[j][1]]-cumlative_sum[queries[j][0]]==0):
                flag_queries[j]=True
        return flag_queries



        