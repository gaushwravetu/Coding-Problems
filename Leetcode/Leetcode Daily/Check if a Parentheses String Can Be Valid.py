class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        # if n<2:
        #     return False
        # i = 0
        # while(i<n):
        #     if s[i]=='(' and s[i+1]=='(' and locked[i+1]=='0':
        #         i+=2
        #     elif s[i]==')' and s[i+1]==')' and locked[i]=='0':
        #         i+=2
        #     elif s[i]==')' and s[i+1]=='(' and locked[i]=='0' and locked[i+1]=='0':
        #         i+=2
        #     elif s[i]=='(' and s[i+1]==')':
        #         i+=2
        #     else:
        #         return False

        # return True
        if len(s) % 2 != 0:
            return False
        
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                return False
        
        stack = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                return False
        
        return True





        