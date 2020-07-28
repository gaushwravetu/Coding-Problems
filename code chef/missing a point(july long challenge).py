from collections import defaultdict
for i in range(int(input())):
    n = int(input())
    resultlist = []
    Xdict = defaultdict(int)
    Ydict = defaultdict(int)
    for j in range(4*n-1):
        Xaxis, Yaxis = map(int,input().split())
        Xdict[Xaxis]+=1
        Ydict[Yaxis]+=1
    for i in Xdict:
        if Xdict[i]%2!=0:
            resultlist.append(i)
            break
    for j in Ydict:
        if Ydict[j]%2!=0:
            resultlist.append(j)
            break
    #print(Xdict,Ydict)
    print(*resultlist)
