class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        total_cost = 0
        for i in range(len(s)):
            if s[i] == t[i]:
                continue
            s_index = ord(s[i]) - ord('a')
            t_index = ord(t[i]) - ord('a')
            forward_distance = (t_index - s_index) % 26
            backward_distance = (s_index - t_index) % 26
            forward_cost = sum(nextCost[(s_index + j) % 26] for j in range(forward_distance))
            backward_cost = sum(previousCost[(s_index - j) % 26] for j in range(backward_distance))
            total_cost += min(forward_cost, backward_cost)
        
        return total_cost




        