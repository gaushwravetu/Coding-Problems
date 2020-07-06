n=2
m=2
(wid,ht,rasin)=map(int,input().split())
ghantaList=[]
d=16
while d>0:
    if wid%d==0 and ht%d==0:
        n=d
        m=d
        break
    d-=1
test=0
while test<n:
    test+=1
    faltu=list(map(int,input().split()))
    ghantaList.append(faltu)

print(n,m,0)