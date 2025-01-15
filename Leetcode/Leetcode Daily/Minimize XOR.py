class Solution:
    def minimizeXor(self, a: int, b: int) -> int:
        countB = bin(b).count('1')
        c = 0

        for i in range(31, -1, -1):
            if (a & (1 << i)) and countB > 0:
                c |= (1 << i)
                countB -= 1
        
        
        for i in range(32):
            if countB == 0:
                break
            if not (c & (1 << i)):
                c |= (1 << i)
                countB -= 1
        
        return c
        