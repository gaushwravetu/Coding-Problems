def calsub(s,n,t,dp):
    dp[0][0]=1
    for i in range(n+1):
        dp[i][0]=1
        for j in range(1,t+1):
            dp[0][j]=0
    for i in range(1,n+1):
        for j in range(1,t+1):
            if s[i-1]<=j:
                dp[i][j] = dp[i-1][j-s[i-1]]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return dp[n][t]

subset = list(map(int,input().split()))
targetDiff = int(input())
n = len(subset)
target = (sum(subset)+targetDiff)//2
print(target)
dp = [[-1 for i in range(target+1)] for i in range(n+1)]
print(calsub(subset,n,target,dp))