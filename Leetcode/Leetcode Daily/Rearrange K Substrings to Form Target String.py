from collections import Counter
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        n = len(s)
        if n % k != 0:
            return False
        
        substring_length = n // k
        s_substrings = [s[i:i + substring_length] for i in range(0, n, substring_length)]
        t_substrings = [t[i:i + substring_length] for i in range(0, n, substring_length)]
        
        return Counter(s_substrings) == Counter(t_substrings)
        