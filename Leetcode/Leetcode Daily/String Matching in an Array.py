class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def compute_lps(pattern):
            """Compute the Longest Prefix which is also Suffix (LPS) array."""
            m = len(pattern)
            lps = [0] * m
            length = 0
            i = 1

            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        def kmp_search(text, pattern):
            """Perform KMP search for a pattern in a given text."""
            n, m = len(text), len(pattern)
            lps = compute_lps(pattern)
            i = j = 0

            while i < n:
                if text[i] == pattern[j]:
                    i += 1
                    j += 1

                if j == m:
                    return True
                elif i < n and text[i] != pattern[j]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return False
                        
        """Find all strings that are substrings of other strings in the array."""
        result = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and kmp_search(other, word):
                    result.append(word)
                    break
        return result


        