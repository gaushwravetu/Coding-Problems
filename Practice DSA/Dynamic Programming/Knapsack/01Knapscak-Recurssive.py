def knapsack(w,v,weight,n):
    if n==0 or weight==0:
        return 0
    if w[n-1]<=weight:
        return max(v[n-1]+knapsack(w,v,weight-w[n-1],n-1),knapsack(w,v,weight,n-1))
    elif w[n-1]>weight:
        return knapsack(w,v,weight,n-1)

weightlist = list(map(int,input().split()))
valuelist = list(map(int,input().split()))
weight = int(input())
n = len(weightlist)
maxout = knapsack(weightlist,valuelist,weight,n)
print(maxout)