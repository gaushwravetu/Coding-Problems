for _ in range(int(input())):
    n = int(input())
    mylist = list(map(int,input().split()))
    mymin = min(mylist)
    resultingIndex = mylist.index(mymin)
    reqSum = sum(mylist[:resultingIndex+1])
    ans = n-(resultingIndex+1)
    v = mymin*ans
    print(reqSum+v)