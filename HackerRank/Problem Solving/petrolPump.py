minCadLen = int(input())
maxCadLen = int(input())
minCadWid = int(input())
maxCadWid = int(input())
total = 0
def check(i,j):
    count = 0
    rssult = i*j
    while(i>0 and j>0):
        count+=1
        if(i>j):
            i-=j
        else:
            j-=i
    return count
if(minCadLen>0 and maxCadLen<1501 and minCadLen<maxCadLen and minCadWid>0 and maxCadWid<1501 and minCadWid<maxCadWid):
    for i in range(minCadLen,maxCadLen):
        for j in range(minCadWid, maxCadWid):
            total+=check(i,j)
print(total)