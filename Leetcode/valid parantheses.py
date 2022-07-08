class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        mystack = []
        for i in range(n):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                mystack.append(s[i])
            else:
                if len(mystack)==0:
                    return False
                else:
                    res = mystack.pop()
                    if (res=='(' and s[i]==')') or (res=='{' and s[i]=='}') or (res=='[' and s[i]==']'):
                        continue
                    else:
                        return False
        if len(mystack)==0:
            return True
        return False
        