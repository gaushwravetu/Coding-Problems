t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    i = len(l)-1
    count = 0
    while i>=0:
        a = l[i]
        b = 0
        c = i-1
        while b<c:
            x = 0
            x =  l[b]+l[c]
            if(x==l[i]):
                count+=1
                b+=1
            elif (x<a):
                b+=1
            else:
                c-=1
        i-=1
    if(count==0):
        print(-1)
    else:
        print(count)
