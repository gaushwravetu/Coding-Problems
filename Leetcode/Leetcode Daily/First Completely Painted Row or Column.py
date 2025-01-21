class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Better Approach
        n,m,k = len(mat),len(mat[0]),len(arr)
        row_count = [0]*n
        column_count = [0]*m
        mydict = {}
        for i in range(n):
            for j in range(m):
                mydict[mat[i][j]] = (i,j)
        
        # print(mydict)
        for i in range(k):
            row,column = mydict[arr[i]][0],mydict[arr[i]][1]
            row_count[row]+=1
            column_count[column]+=1

            if row_count[row]==m or column_count[column]==n:
                return i