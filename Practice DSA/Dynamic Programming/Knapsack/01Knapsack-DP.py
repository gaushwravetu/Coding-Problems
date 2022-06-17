def knapsack(w,v,wt,n,dp):
    for i in range(n+1):
        for j in range(wt+1):
            if i==0 or j==0:
                dp[i][j]==0
    for i in range(1,n+1):
        for j in range(1,wt+1):
            if w[i-1]<=j:
                dp[i][j] = max(v[i-1]+dp[i-1][j-w[i-1]],dp[i-1][i])
            elif w[i-1]>j:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return dp[n][wt]+1

weightlist = list(map(int,input().split()))
valuelist = list(map(int,input().split()))
weight = int(input())
n = len(weightlist)
dp = [[-1 for x in range(weight+1)] for x in range(n+1)]
maxout = knapsack(weightlist,valuelist,weight,n,dp)
print(maxout)