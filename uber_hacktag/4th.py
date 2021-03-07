def findLayers(m,n,locker):
    r=0
    c=0
    fullMat=[]
    while r<n and c<m:
        layer=[]
        for i in range(c, m):
            layer.append(locker[r][i])
        r+=1
        for i in range(r,n):
            layer.append(locker[i][m-1])
        m-=1
        if r<n:
            for i in range(m-1,c-1,-1):
                layer.append(locker[n-1][i])
            n-=1
        if c<m:
            for i in range(n-1, r-1, -1):
                layer.append(locker[i][c])
            c+=1
        layer.sort()
        fullMat.append(layer)
    return fullMat
arr = [[9,7,-4,5],[1,6,2,-6],[12,20,2,0]]
print(findLayers(2,2,arr))