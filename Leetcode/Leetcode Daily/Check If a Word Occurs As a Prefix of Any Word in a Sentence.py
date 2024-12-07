class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        count = 0
        size_sw = len(searchWord)
        for word in sentence.split():
            count+=1
            if word[:size_sw]==searchWord:
                return count
        return -1
        