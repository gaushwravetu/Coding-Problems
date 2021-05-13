def Arrical_maze(N,M,Q,Mag,Arr):
    mymax = 0
    if Arr[1][1]==-1 or Arr[M][N]==-1:
        return 0
    for i in range(1,M+1):
        if Arr[i][1]==0:
            Arr[i][1]=1
        else:
            break
    for j in range(2,N+1):
        if Arr[1][j]==0:
            Arr[1][j]=1
        else:
            break
    for i in range(2,M+1):
        for j in range(2,N+1):
            if Arr[i][j]==-1:
                continue
            else:
                if Arr[i-1][j]>=0:
                    Arr[i][j]=Arr[i-1][j]+Arr[i][j]
                if Arr[i][j-1]>=0:
                    Arr[i][j]=Arr[i][j]+Arr[i][j-1]
                    
    

