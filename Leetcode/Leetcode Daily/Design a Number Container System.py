class NumberContainers:

    def __init__(self):
        self.index_to_number = {}  # Maps index -> number
        self.number_to_indices = {}  # Maps number -> SortedSet of indices
        

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.number_to_indices:
                self.number_to_indices[old_number].discard(index)
                if not self.number_to_indices[old_number]:
                    del self.number_to_indices[old_number]

        self.index_to_number[index] = number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = SortedSet()
        self.number_to_indices[number].add(index)
        

    def find(self, number: int) -> int:
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)