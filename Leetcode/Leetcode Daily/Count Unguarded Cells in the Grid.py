class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def markguarded(row,col,home):
            # traversing UP side of the home and marking it 1 means guarded
            k = row-1
            while(k>=0):
                if(home[k][col]==2 or home[k][col]==3):
                    break
                home[k][col] = 1 #marked as guarded
                k-=1
            
            # traversing DOWN side of the home and marking it 1 means guarded
            k = row+1
            while(k<len(home)):
                if(home[k][col]==2 or home[k][col]==3):
                    break
                home[k][col] = 1 #marked as guarded
                k+=1
            
            # traversing LEFT side of the home and marking it 1 means guarded
            k = col-1
            while(k>=0):
                if(home[row][k]==2 or home[row][k]==3):
                    break
                home[row][k] = 1 #marked as guarded
                k-=1
            
            # traversing RIGHT side of the home and marking it 1 means guarded
            k = col+1
            while(k<len(home[0])):
                if(home[row][k]==2 or home[row][k]==3):
                    break
                home[row][k] = 1 #marked as guarded
                k+=1


        # Initiliazing the 2D List to mark gurard, wall and further opreations
        home = [[0 for _ in range(n)] for _ in range(m)]
        # Marking all the gurards with 2
        for k in guards:
            i = k[0]
            j = k[1]
            home[i][j] = 2
        # Marking all the walls with 3
        for k in walls:
            i = k[0]
            j = k[1]
            home[i][j] = 3

        for k in guards:
            i = k[0]
            j = k[1]
            markguarded(i,j,home)
        # print(home)
        count = 0
        for i in range(len(home)):
            for j in range(len(home[i])):
                if home[i][j]==0:
                    count+=1
        return count
        