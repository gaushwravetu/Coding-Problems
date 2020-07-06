for _ in range(int(input())):
    N,Flavours = map(int,input().split())
    Flavourslist = list(map(int,input().split()))
    maxlenset = {}
    (mymax,result) = (0,0)
    for i in Flavourslist:
        mymaxlenset.add(i)
        for j in range(i+1,N):
            if(len(mymaxlenset)=Flavours):
                mymax = len(mymaxlenset)
                mymaxlenset.clear()
                break
            else:
                mymaxlenset.add(j)
        result = max(mymax,result)
    print(result)
