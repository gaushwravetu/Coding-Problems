class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        def isPrefixAndSuffix(a,b):
            if len(a)>len(b):
                return False
            elif a == b[0:len(a)] and a==b[len(b)-len(a):len(b)]:
                return True
        for i in range(n-1):
            for j in range(i+1,n):
                if(isPrefixAndSuffix(words[i],words[j])):
                    count+=1
        return count
        