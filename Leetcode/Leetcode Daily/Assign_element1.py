from typing import List

def assign_elements(groups: List[int], elements: List[int]) -> List[int]:
    n = len(groups)
    m = len(elements)
    assigned = [-1] * n
    
    # Preprocess elements: store the smallest index for each unique element value
    element_map = {}
    for j in range(m):
        if elements[j] not in element_map:
            element_map[elements[j]] = j
    
    # Iterate over each group
    for i in range(n):
        group_size = groups[i]
        min_index = float('inf')
        
        # Find all divisors of group_size and check if they exist in element_map
        d = 1
        while d * d <= group_size:
            if group_size % d == 0:
                # Check divisor d
                if d in element_map:
                    min_index = min(min_index, element_map[d])
                # Check divisor group_size // d
                if d != group_size // d and (group_size // d) in element_map:
                    min_index = min(min_index, element_map[group_size // d])
            d += 1
        
        # Assign the smallest index or -1 if no divisor found
        assigned[i] = min_index if min_index != float('inf') else -1
    
    return assigned
