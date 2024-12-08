class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
            
        if is_prime(n):
            return -1
        
        n_str, m_str = str(n), str(m)
        if len(n_str) != len(m_str):
            return -1
            
        def generate_next_numbers(num):
            num_str = str(num)
            next_numbers = []
            for i in range(len(num_str)):
                digit = int(num_str[i])
                if digit < 9:
                    next_numbers.append(num_str[:i] + str(digit + 1) + num_str[i + 1:])
                if digit > 0:
                    next_numbers.append(num_str[:i] + str(digit - 1) + num_str[i + 1:])
            return next_numbers
    
        min_heap = [(n, n)]  # (current cost, current number)
        visited = set([n])
        while min_heap:
            cost, current = heapq.heappop(min_heap)
            if current == m:
                return cost
            for next_num_str in generate_next_numbers(current):
                next_num = int(next_num_str)
                if next_num in visited or is_prime(next_num):
                    continue
                visited.add(next_num)
                heapq.heappush(min_heap, (cost + next_num, next_num))  # Push with updated cost
        return -1
        