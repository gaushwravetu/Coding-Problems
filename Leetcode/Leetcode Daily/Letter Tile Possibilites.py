from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def backtrack(counter):
            nonlocal count
            for char in counter:
                if counter[char] > 0:
                    count += 1
                    counter[char] -= 1
                    backtrack(counter)
                    counter[char] += 1
        count = 0
        counter = Counter(tiles)
        backtrack(counter)
        return count
        