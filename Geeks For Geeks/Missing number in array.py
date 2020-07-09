t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    mysum = int(n*(n+1)/2)
    series_sum = 0
    #print(mysum)
    for i in range(len(l)):
        series_sum+=l[i]
    result = int(mysum - series_sum)
    print(result)