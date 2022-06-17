def LCS_Recurssive(s,t,sl,tl):
    if sl==0 or tl==0:
        return 0
    if t[tl-1]==s[sl-1]:
        return 1+LCS_Recurssive(s,t,sl-1,tl-1)
    else:
        return max(LCS_Recurssive(s,t,sl-1,tl),LCS_Recurssive(s,t,sl,tl-1))


sourceString = input()
targetString = input()
slen = len(sourceString)
tlen = len(targetString)

print(LCS_Recurssive(sourceString,targetString,slen,tlen))
