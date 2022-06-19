def lcs_topdown(s,t,sl,tl,dp):
    for i in range(slen+1):
        dp[i][0] = 0
        for j in range(tlen+1):
            dp[0][j] = 0
    for i in range(1,slen+1):
        for j in range(1,tlen+1):
            if s[i-1]==t[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    print(dp)
    return dp[sl][tl]
sourceString = input()
targetString = input()
slen = len(sourceString)
tlen = len(targetString)

dp = [[-1 for i in range(tlen+1)] for i in range(slen+1)]
print(lcs_topdown(sourceString,targetString,slen,tlen,dp))