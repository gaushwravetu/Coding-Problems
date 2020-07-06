def minswapfunc(Vases): 
    n = len(Vases) 
    PositionList = [*enumerate(Vases)] 
    PositionList.sort(key = lambda it:it[1]) 
    VisitedList = {k:False for k in range(n)} 
    result = 0
    for i in range(n): 
        if VisitedList[i] or PositionList[i][0] == i: 
            continue
        swapCount = 0
        j = i 
        while not VisitedList[j]: 
            VisitedList[j] = True
            j = PositionList[j][0] 
            swapCount += 1
        if swapCount > 0: 
            result += (swapCount - 1) 
    return result
for _ in range(int(input())):
    N,M = map(int,input().split())
    listOfVases = list(map(int,input().split()))
    robotlist = []
    for j in range(M):
        Xi,Yi = map(int,input().split())
        robotlist.append((Xi,Yi))
    myresult = minswapfunc(listOfVases)
    if(M==0):
        print(myresult)
        continue
    print(myresult-1)
        
        