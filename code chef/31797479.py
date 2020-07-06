for i in range(int(input())):
    N,M,K = map(int,input().split())
    mylist = []
    for i in range(N):
        mylist.append(list(map(int,input().split())))
        ans=[]
    runningList=[]
    for i in range(N):
        temp=[]
        for j in range(K):
            temp.append(mylist[i][j])
        runningList.append(temp)
    for i in range(N):
        countarry = [0 for x in range(M+1)]
        for j in range(K):
            countarry[mylist[i][j]]+=1
        ans.append((max(countarry),countarry.index(max(countarry)),i))
    accuracy=[]
    for j in range(K):
        score=0
        for i in range(N):
            score+=ans[i][1]==mylist[i][j]
        accuracy.append((score,j))
    accuracy.sort()
    ans.sort()
    prevmin=accuracy[0][0]
    prevans=ans.copy()
    
    while True:
        r=ans[0][2];c=accuracy[0][1];
        for i in range(K):
            runningList[r][i]=runningList[r][c]
        ans=[]
        for i in range(N):
            countarry = [0 for x in range(M+1)]
            for j in range(K):
                countarry[runningList[i][j]]+=1
            ans.append((max(countarry),countarry.index(max(countarry)),i))
        accuracy=[]
        for j in range(K):
            score=0
            for i in range(N):
                score+=ans[i][1]==mylist[i][j]
            accuracy.append((score,j))
        accuracy.sort()
        ans.sort()
        if accuracy[0][0]<=prevmin:
            ans=prevans
            break
        prevmin=accuracy[0][0]
        prevans=ans.copy()
        
    res=[0]*N
    for x in ans:
        res[x[2]]=x[1]
    print(*res)
    