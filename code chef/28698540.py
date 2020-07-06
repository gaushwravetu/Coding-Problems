#doraemon problem
def sample(mat,i,j):
    x = 1
    count = 0
    while(i-x >=0 and i+x<r and j-x>=0 and j+x<c):
        if(mat[i-x][j]==mat[i+x][j] and mat[i][j-x]==mat[i][j+x]):
            count+=1
            x+=1
        else:
            break
    return(count)   
t = int(input())
for i in range(t):
    r, c = list(map(int,input().split()))
    mat = []
    sum = 0
    for i in range(r):
        mat.append(list(map(int,input().split())))
    for i in range(1,r):
        for j in range(1,c):
           sum+=sample(mat,i,j)
    print(r*c+sum)