from collections import Counter
from typing import List
class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # count_zero,count_one = 0,0
        # n = len(matrix)
        # for i in range(n):
        #     flag = matrix[i][0]
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j]!=flag:
        #             if i==0 and matrix[i+1][j]==flag:
        #                 matrix[i][j],matrix[i+1][j] = matrix[i+1][j],matrix[i][j]
        #             elif i>0 and matrix[i+1][j]==flag:
        #                 matrix[i][j],matrix[i+1][j] = matrix[i+1][j],matrix[i][j]
        #             elif (i>0 or i==n-1) and matrix[i-1][j]==flag:
        #                 matrix[i][j],matrix[i-1][j] = matrix[i-1][j],matrix[i][j]
        # for i in matrix:
        #     if len(set(i))==1:
        #         if i[0]==0:
        #             count_zero+=1
        #         else:
        #             count_one+=1
        # return max(count_zero,count_one)
        pattern_count = Counter()
        for row in matrix:
            # Normalize the row pattern
            # Create a pattern where the first element is always 0
            pattern = tuple(x ^ row[0] for x in row)
            pattern_count[pattern] += 1
        
        # Return the maximum count of any pattern
        return max(pattern_count.values())

                    
