class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        result = [0]*n
        mysum = 0
        for i in shifts:
            if i[2]==0:
                if i[1]+1<n:
                    result[i[1]+1]+=1
                result[i[0]]-=1
            else:
                if i[1]+1<n:
                    result[i[1]+1]-=1
                result[i[0]]+=1
        # print(result)
        resultstr = ""
        for i in range(n):
            mysum+=result[i]
            resultstr+=chr((ord(s[i])-ord('a')+mysum)%26 + ord('a'))

        return resultstr
