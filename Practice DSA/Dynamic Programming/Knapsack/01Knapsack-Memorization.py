def knapsack(w,v,weight,n,dp):
    if n==0 or weight==0:
        return 0
    if dp[n][weight]!=-1:
        return dp[n][weight]    
    if w[n-1]<=weight:
        dp[n][weight] = max(v[n-1]+knapsack(w,v,weight-w[n-1],n-1,dp),knapsack(w,v,weight,n-1,dp))
        return max(v[n-1]+knapsack(w,v,weight-w[n-1],n-1,dp),knapsack(w,v,weight,n-1,dp))
    elif w[n-1]>weight:
        dp[n][weight] = knapsack(w,v,weight,n-1,dp)
        return knapsack(w,v,weight,n-1,dp)

weightlist = list(map(int,input().split()))
valuelist = list(map(int,input().split()))
weight = int(input())
n = len(weightlist)
dp = [[-1 for x in range(weight+1)] for x in range(n+1)]
maxout = knapsack(weightlist,valuelist,weight,n,dp)
print(maxout)