class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define vowels
        vowels = set("aeiouAEIOU")
        # Convert string to a list to allow modification
        s = list(s)
        
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer until a vowel is found
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer until a vowel is found
            while left < right and s[right] not in vowels:
                right -= 1
            # Swap the vowels
            s[left], s[right] = s[right], s[left]
            # Move pointers inward
            left += 1
            right -= 1
        
        # Join the list back into a string
        return ''.join(s)