class Solution:

    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def isSubset(A,B):
            for i in range(0,26):
                if A[i]<B[i]:
                    return False
            return True
            
        freq_count = [0]*26
        result = []
        for i,word in enumerate(words2):
            check_char = [0]*26
            for j in word:
                check_char[ord(j)-ord('a')]+=1
                freq_count[ord(j)-ord('a')] = max(freq_count[ord(j)-ord('a')],check_char[ord(j)-ord('a')])

        for i,word in enumerate(words1):
            check_char = [0]*26
            for j in word:
                check_char[ord(j)-ord('a')]+=1
            
            if(isSubset(check_char,freq_count)):
                result.append(word)

        return result

        
        