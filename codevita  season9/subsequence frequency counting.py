from collections import defaultdict
for i in range(int(input())):
    n = int(input())
    mylist = list(map(int,input().split()))
    resultlist = []
    mod = 10**9+7
    mydict = defaultdict(int)
    for i in mylist:
        mydict[i]+=1
    for i in range(n-1):
        for j in range(i+1,n):
            minres = min(mylist[i:j+2])
            print(mylist[i:j+2])
            mydict[minres]+=1
            print(mylist[i],mylist[j])
            minres = min(mylist[i],mylist[j])
            mydict[minres]+=1
    for i in mylist:
        resultlist.append(mydict[i])
    print(*resultlist)