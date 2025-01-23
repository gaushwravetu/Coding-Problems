class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        rowcount =[0]*n
        colcount = [0]*m
        connection = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    rowcount[i]+=1
                    colcount[j]+=1

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    if rowcount[i]>1:
                        connection+=1
                    elif colcount[j]>1:
                        connection+=1

        return connection
