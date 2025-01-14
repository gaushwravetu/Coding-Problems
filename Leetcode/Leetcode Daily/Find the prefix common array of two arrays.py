class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = set()
        common_count = 0
        result = []

        for i in range(len(A)):
            if A[i] in seen:
                common_count += 1
            if B[i] in seen:
                common_count += 1
            if A[i] == B[i]:
                common_count += 1
            seen.add(A[i])
            seen.add(B[i])
            result.append(common_count)

        return result
        

        