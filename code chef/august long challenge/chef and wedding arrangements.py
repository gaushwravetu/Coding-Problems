from collections import defaultdict
for i in range(int(input())):
    guest,cost = map(int,input().split())
    guestlist = list(map(int,input().split()))
    guestdict = defaultdict(int)
    result = 1
    for i in guestlist:
        if i not in guestdict:
            guestdict[i]+=1
        else:
            result+=1
            guestdict = defaultdict(int)
            guestdict[i]+=1
    print(result)





