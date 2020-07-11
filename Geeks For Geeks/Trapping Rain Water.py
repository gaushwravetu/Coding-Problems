for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l_max = l[0]
    r_max = max(l[1:])
    r = 0
    for i in range(n):
        if(l[i]>l_max):
            l_max = l[i]
        if(l[i]==r_max and i<n-1):
            r_max = max(l[i+1:])
        r1=min(l_max,r_max)
        r+=max(r1-l[i],0)
    print(r)