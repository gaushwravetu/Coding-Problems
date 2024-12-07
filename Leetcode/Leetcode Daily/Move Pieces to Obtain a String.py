class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j, strlen = 0, 0, len(start)
        while i < strlen or j < strlen:
            # Skip underscores in start and target
            while i < strlen and start[i] == '_':
                i += 1
            while j < strlen and target[j] == '_':
                j += 1
            
            # If both pointers are out of bounds, transformation is valid
            if i == strlen and j == strlen:
                return True
            
            # If one pointer is out of bounds but not the other, transformation is invalid
            if i == strlen or j == strlen:
                return False
            
            # If the characters at i and j are different, transformation is invalid
            if start[i] != target[j]:
                return False
            
            # Validate movement constraints
            if start[i] == 'L' and i < j:  # 'L' cannot move right
                return False
            if start[i] == 'R' and i > j:  # 'R' cannot move left
                return False
            
            # Move both pointers
            i += 1
            j += 1
        
        return True