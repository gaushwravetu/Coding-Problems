class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while(True):
            index = s.find(part)
            if index != -1:
                s = s[:index] + s[index + len(part):]
            else:
                break
        return s