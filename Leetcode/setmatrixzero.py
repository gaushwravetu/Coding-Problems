from collections import defaultdict
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        mydict = defaultdict(list)
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    mydict['i'].append(i)
                    mydict['j'].append(j)
        for i in range(n):
            for j in range(m):
                if ((i in mydict['i']) or (j in mydict['j'])):
                    matrix[i][j]=0
        # print(mydict)
        return matrix
        