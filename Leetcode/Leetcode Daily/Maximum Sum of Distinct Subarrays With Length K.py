class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Brute Force Technique
        # n = len(nums)
        # result = 0
        # for i in range(n):
        #     if i+k<n+1:
        #         temp = []
        #         temp = nums[i:i+k]
        #         if len(set(temp))==len(nums[i:i+k]):
        #             result = max(result,sum(nums[i:i+k]))
        # return result
        n = len(nums)
        uniset = set()
        result,currentwindowsum = 0,0
        i,j = 0,0
        while(j<n):
            # Checking if the current windown is already present in the set, if yes then, i have to shrink my current window
            while(nums[j] in uniset):
                currentwindowsum-=nums[i]
                uniset.remove(nums[i])
                i+=1
            currentwindowsum+=nums[j]
            uniset.add(nums[j])
            if(j-i+1==k):
                result = max(result,currentwindowsum)
                uniset.remove(nums[i])
                currentwindowsum-=nums[i]
                i+=1
            j+=1
        return result



        