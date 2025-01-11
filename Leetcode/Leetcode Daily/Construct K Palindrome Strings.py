class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        strdict = {}
        count = 0
        for i in s:
            if i in strdict:
                strdict[i]+=1
            else:
                strdict[i]=1
        for i in strdict:
            if strdict[i]%2==1:
                count+=1
        if count>k or k>len(s):
            return False
        
        return True
