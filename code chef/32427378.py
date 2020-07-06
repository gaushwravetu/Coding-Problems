from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    m = int(input())
    B = list(map(int,input().split()))
    mydictB = defaultdict(int)
    for i in B:
        mydictB[i]+=1
    (k,count,flag) = (0,0,0)
    for i in range(n):
        if(l[i] in mydictB):
            if(flag==0):
                flag=1
                count+=1
        else:
            flag=0
    print(count)
        
            