for _ in range(int(input())):
    n = int(input())
    count = 0
    #mysum = 0
    l1 = list(map(int,input().split()))
    for i in range(n):
        if(l1[i]%2==0):
            count+=1
    print(count*(n-count))
