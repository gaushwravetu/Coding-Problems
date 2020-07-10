for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    k = int(input())
    prev_result = 10000000000
    for i in range(n-k+1):
        curr_result = arr[i+k-1]-arr[i]
        #print(curr_result)
        if(curr_result<prev_result):
            prev_result = curr_result
    print(prev_result)