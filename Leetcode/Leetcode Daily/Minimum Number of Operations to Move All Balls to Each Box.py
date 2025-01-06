class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Brute Force approach
        # occurance_1 = []
        # result = []
        # n = len(boxes)
        # for i in range(n):
        #     if boxes[i]=='1':
        #         occurance_1.append(i)
        # for j in range(n):
        #     ans = 0
        #     for k in occurance_1:
        #         ans+=abs(j-k)
        #     result.append(ans)
        # return result

        n = len(boxes)
        result = [0] * n
        
        # Left pass
        count = 0
        operations = 0
        for i in range(n):
            result[i] += operations
            count += int(boxes[i])
            operations += count 
        
        # Right pass
        count = 0
        operations = 0
        for i in range(n - 1, -1, -1):
            result[i] += operations
            count += int(boxes[i])
            operations += count
        
        return result
        
                