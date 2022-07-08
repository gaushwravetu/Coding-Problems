class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix[0])-1
        n = len(matrix)
        m = len(matrix[0])
        
        while(start>=0 and start<n and end>=0 and end<m):
            if matrix[start][end]==target:
                return True
            elif matrix[start][end]<target:
                start+=1
            elif matrix[start][end]>target:
                end-=1
        return False
            
        