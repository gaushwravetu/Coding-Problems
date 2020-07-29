from collections import defaultdict
def SequenceChecker(ad, bd, abd, mymin):
    atob = []
    btoa = []
    cost = 0
    for i in abd:
        if abd[i]%2!=0:
            return -1
        elif(i in ad or i in bd):
            if ad[i]==None:
                ad[i]=0
            if bd[i]==None:
                bd[i]=0
            if ad[i]==bd[i]:
                continue
            elif ad[i]>bd[i]:
                for x in range((ad[i]-bd[i])//2):
                    atob.append(i)
            else:
                for x in range((bd[i]-ad[i])//2):
                    btoa.append(i)
    lenatob = len(atob)
    lenbtoa = len(btoa)
    if lenatob==0 and lenbtoa==0:
        return cost
    if lenatob!=lenbtoa:
        return -1
    atob.sort()
    btoa.sort(reverse=True)
    for i in range(lenatob):
        cost+= min(2*mymin, min(atob[i],btoa[i]))
    return cost
    
for i in range(int(input())):
    n = int(input())
    adict = defaultdict(int)
    bdict = defaultdict(int)
    abdict = defaultdict(int)
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    mymin = min(a)
    mymin = min(mymin,min(b))
    for i in range(n):
        adict[a[i]]+=1
        bdict[b[i]]+=1
        abdict[a[i]]+=1
        abdict[b[i]]+=1
    result = SequenceChecker(adict,bdict,abdict,mymin)
    print(result)
