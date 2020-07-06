for _ in range(int(input())):
    (N,a,b,c)=map(int,input().split())
    Flist=list(map(int, input().split()))
    minTime=10**10
    for x in Flist:
        thisTime=abs(b-x)+abs(x-a)
        if thisTime<minTime:
            minTime=thisTime
    minTime+=c
    print(minTime)
        