class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0]*n
        extended_array = code+code
        if k == 0:
            return [0]*(n)
        for i in range(n):
            if k>0:
                for j in range(i+1,i+k+1):
                    result[i]+=code[j%n]
            if k<0:
                for j in range(i-abs(k),i):
                    result[i]+=code[(j+n)%n]
        return result

        