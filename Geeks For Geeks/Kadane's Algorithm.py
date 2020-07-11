#2nd approach
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    local_sum = l[0]
    global_sum = l[0]
    for j in range(1,len(l)):
        local_sum = max(l[j],local_sum+l[j])
        global_sum = max(local_sum,global_sum)
    print(global_sum)