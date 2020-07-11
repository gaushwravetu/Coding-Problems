for _ in range(int(input())):
    t = int(input())
    l = list(map(int,input().split()))
    n = int(input())
    l.sort()
    #print(l)
    print(l[n-1])
    
    