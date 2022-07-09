from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = defaultdict(int)
        n = len(nums)
        for i in range(n):
            mydict[nums[i]]=(i)
#         for i in mydict:
#             res=target
#             res-=i
#             mydict[i][1]=True
#             if (res in mydict and mydict[i][1]==False):
#                 return(mydict[i][0],mydict[res][0])
#             mydict[i][1]=False
        for i in range(n):
            res = target
            res-=nums.pop(0)
            if res in nums:
                return(i,mydict[res])
        



                
        