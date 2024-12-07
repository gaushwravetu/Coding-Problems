class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result,neg_count,min_element = 0,0,10**5
        for i in range(len(matrix)):
            for j in (matrix[i]):
                if j<0:
                    neg_count+=1
                result+=abs(j)
                min_element = min(abs(j),min_element)
        if neg_count%2==1:
            print(min_element)
            return (result-min_element*2)
        return result
                
        