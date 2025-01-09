class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for index,word in enumerate(words):
            if len(word)>=len(pref) and pref == word[:len(pref)]:
                count+=1
        return count
        