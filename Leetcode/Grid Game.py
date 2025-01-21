class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # calculating 1st row sum
        m = len(grid[0])
        first_row_sum = sum(grid[0])
        second_row_sum,best_of_robot2 = 0,0
        min_result = float('inf')

        for i in range(m):
            first_row_sum-=grid[0][i]
            best_of_robot2 = max(first_row_sum,second_row_sum)
            second_row_sum+=grid[1][i]

            min_result = min(min_result,best_of_robot2)
        
        return min_result
        