class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def ispossible(nums,maxop,mid):
            result = 0
            for i in nums:
                ops = i//mid
                if(i%mid==0):
                    ops-=1
                result+=ops
            if result>maxop:
                return False
            return True
        # time complexity = O(n*Log(max(nums)))
        left = 1
        right = max(nums)
        while(right>=left):
            mid = left + (right-left)//2
            if(ispossible(nums,maxOperations,mid)):
                answer = mid
                right = mid-1
            else:
                left = mid+1
        return answer