class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        count1 = 0
        i = n-1
        temp1,temp0=0,0
        result = float('-inf')
        while(i>=0):
            if s[i]=='1':
                count1+=1
            i-=1
        for j in range(n-1):
            if s[j]=='1':
                temp1+=1
            else:
                temp0+=1
            
            result = max(result, temp0+count1-temp1)
        
        return result
