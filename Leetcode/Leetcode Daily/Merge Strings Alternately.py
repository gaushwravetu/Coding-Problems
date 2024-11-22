class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_w1 = len(word1)
        len_w2 = len(word2)
        total_len = len_w1+len_w2
        i,j=0,0
        result = ""
        for k in range(total_len):
            if i<len_w1:
                result+=word1[i]
                i+=1
            # else:
            #     result+=word2[j:len_w2]
            if j<len_w2:
                result+=word2[j]
                j+=1
            # else:
            #     result+=word1[i:len_w1]

        return result