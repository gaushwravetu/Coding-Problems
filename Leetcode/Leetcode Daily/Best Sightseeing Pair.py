class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # I'll create a list which stores the highest value till each index, max(values[i]+i)
        max_i = []
        n = len(values)
        new_max,result = float('-inf'),float('-inf')
        for i in range(n):
            new_max = max(new_max,values[i]+i)
            max_i.append(new_max)
        # Now I'll check for each jth index which is the max suitable value from left since i<j:
        j = 1
        while(j<n):
            i = j-1
            result = max(result, max_i[i]+values[j]-j)
            j+=1

        return result
        