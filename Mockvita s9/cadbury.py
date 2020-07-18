minCadLen = int(input())
maxCadLen = int(input())
minCadWid = int(input())
maxCadWid = int(input())
total = 0
def check(i,j):
    count = 0
    #rssult = i*j
    while(i>0 and j>0):
        count+=1
        if(i>j):
            i-=j
        else:
            j-=i
    return count
        for i in range(minCadLen,maxCadLen):
            for j in range(minCadWid, maxCadWid):
                total+=check(i,j)
print(total)
