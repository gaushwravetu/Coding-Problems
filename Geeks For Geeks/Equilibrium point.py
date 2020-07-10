t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    result = 0
    lsum = 0
    flag = False
    for i in range(n):
        result+=l[i]
    for i in range(n):
        if(not flag):
            result-=l[i]
            if lsum==result:
                flag = True
                print(i+1)
                break
            lsum+=l[i]
    if(not flag):
        print(-1)
    
        