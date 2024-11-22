class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        # checking if GCD is valid or not
        if str1+str2!=str2+str1:
            return result
        else:
            k = gcd(len(str1),len(str2))
            result = str1[:k]
            return result
        