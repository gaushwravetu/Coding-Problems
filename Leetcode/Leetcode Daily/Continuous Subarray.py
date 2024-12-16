from sortedcontainers import SortedDict
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        mydict = SortedDict()
        n = len(nums)
        j,i = 0,0
        count = 0
        # Using sliding window and ordered map(orederd dictionary) to track min and max
        while(j<n):
            if nums[j] not in mydict:
                mydict[nums[j]]=1
            else:
                mydict[nums[j]]+=1

            while(abs(mydict.peekitem(-1)[0]-mydict.peekitem(0)[0])>2):
                mydict[nums[i]]-=1
                if mydict[nums[i]]==0:
                    del mydict[nums[i]]
                i+=1
            
            count+=j-i+1
            j+=1
        return count
    
            
    
        