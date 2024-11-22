class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count_zero,count_one = 0,0
        n = len(matrix)
        for i in range(n):
            flag = matrix[i][0]
            for j in range(len(matrix[i])):
                if matrix[i][j]!=flag:
                    if i==0 and matrix[i+1][j]==flag:
                        matrix[i][j],matrix[i+1][j] = matrix[i+1][j],matrix[i][j]
                    elif i>0 and matrix[i+1][j]==flag:
                        matrix[i][j],matrix[i+1][j] = matrix[i+1][j],matrix[i][j]
                    elif (i>0 or i==n-1) and matrix[i-1][j]==flag:
                        matrix[i][j],matrix[i-1][j] = matrix[i-1][j],matrix[i][j]
        for i in matrix:
            if len(set(i))==1:
                if i[0]==0:
                    count_zero+=1
                else:
                    count_one+=1
        return max(count_zero,count_one)

                    
