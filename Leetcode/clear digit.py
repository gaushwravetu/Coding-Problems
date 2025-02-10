class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        result = list("")
        for i in range(n):
            
            if s[i].isdigit():
                if result:
                    result.pop()
            else:
                result.append(s[i])

        return "".join(result)