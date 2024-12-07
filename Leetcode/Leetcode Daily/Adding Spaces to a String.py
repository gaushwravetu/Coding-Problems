class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # brute Force approach
        count = 0
        # n = len(spaces)
        # for i in range(n):
        #     spaces[i]+=count
        #     s = s[:spaces[i]] + " " + s[spaces[i]:]
        #     count+=1
        # return s
        string_len = len(s)
        modified_s = ""
        if spaces[0]==0:
            modified_s+=' '
        spaces = set(spaces)
        for i in range(string_len):
            modified_s+=s[i]
            if i+1 in spaces:
                modified_s+=' '
        return modified_s