class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()
        count_occurance_left = set()
        count_occurance_right = Counter(s)

        for middle in s:
            count_occurance_right[middle]-=1
            for mychar in count_occurance_left:
                if count_occurance_right[mychar]>0:
                    result.add((middle,mychar))
            count_occurance_left.add(middle)
        return len(result)
        