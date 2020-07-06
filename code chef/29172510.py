t = int(input())
for _ in range(t):
    n = int(input())
    l1 = []
    for  _  in range(n):
        s,p,v = list(map(int,input().split()))
        profit = int(int(p//(s+1))*v)
        l1.append(profit)
    print(max(l1))
        