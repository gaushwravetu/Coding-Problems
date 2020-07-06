for t in range(int(input())):
    n,r = list(map(int,input().split()))
    l = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum+=l[i]
    n = int(sum%r)
    print(n)