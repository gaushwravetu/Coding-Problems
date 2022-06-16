def calsubset(s,t,dp,n):
    for i in range(n+1):
        for j in range(t+1):
            if i==0:
                dp[i][j]=False
            elif j==0:
                dp[i][j]=True
    for i in range(1,n+1):
        for j in range(1,t+1):
            if s[i-1]<=j:
                dp[i][j] = dp[i-1][j-s[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return dp[n][t]

subset = list(map(int,input().split()))
target = int(input())
n = len(subset)
dp = [[-1 for x in range(target+1)] for x in range(n+1)]
result = calsubset(subset,target,dp,n)
print(result)