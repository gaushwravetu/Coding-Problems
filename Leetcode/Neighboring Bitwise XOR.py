class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        # starting from 0
        start = 0
        for i,element in enumerate(derived):
            if i == n-1 and derived[n-1] == start^0:
                return True
            start = element^start
            # print(start)
        # print('---------------')
        start = 1
        for i,element in enumerate(derived):
            if i == n-1 and derived[n-1] == start^1:
                return True
            start = element^start
            # print(start)

        return False





        