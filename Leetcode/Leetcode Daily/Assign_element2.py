class Solution:
    def assignElements(self, groups_list: List[int], elements_list: List[int]) -> List[int]:

        def build_number_index_map(elements_list: List[int]) -> dict:
            number_index_map = {}
            index = 0
            while index < len(elements_list):
                if elements_list[index] not in number_index_map:
                    number_index_map[elements_list[index]] = index
                index += 1
            return number_index_map

        
        def find_smallest_divisor_index(group_value: int, number_index_map: dict) -> int:
            smallest_index = float('inf')
            divisor = 1
            while divisor * divisor <= group_value:
                if group_value % divisor == 0:
                    paired_divisor = group_value // divisor
                    
                    if divisor in number_index_map:
                        smallest_index = min(smallest_index, number_index_map[divisor])
                    if paired_divisor != divisor and paired_divisor in number_index_map:
                        smallest_index = min(smallest_index, number_index_map[paired_divisor])
                divisor += 1
            return -1 if smallest_index == float('inf') else smallest_index

        
        number_index_map = build_number_index_map(elements_list)
        result_indices = []
        
        for group_value in groups_list:
            result_indices.append(find_smallest_divisor_index(group_value, number_index_map))
        
        return result_indices

        