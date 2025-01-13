class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        deleted = 0
        if n<3:
            return n
        visited = [0]*26
        for i in range(n):
            visited[ord(s[i])-ord('a')]+=1
            if visited[ord(s[i])-ord('a')]==3:
                visited[ord(s[i])-ord('a')]-=2
                deleted+=2
        return n-deleted

        