def lcs_mem(s,t,sl,tl,dp):
    if sl==0 or tl==0:
        return 0
    if dp[sl][tl]!=-1:
        return dp[sl][tl]
    elif s[sl-1]==t[tl-1]:
        dp[sl][tl] = 1+lcs_mem(s,t,sl-1,tl-1,dp)
        return 1+lcs_mem(s,t,sl-1,tl-1,dp)
    else:
        dp[sl][tl] = max(lcs_mem(s,t,sl-1,tl,dp),lcs_mem(s,t,sl,tl-1,dp))
        return max(lcs_mem(s,t,sl-1,tl,dp),lcs_mem(s,t,sl,tl-1,dp))

sourceString = (input())
targetString = (input())
slen = len(sourceString)
tlen = len(targetString)

dp = [[-1 for i in range(tlen+1)] for x in range(slen+1)]
print(lcs_mem(sourceString,targetString,slen,tlen,dp))