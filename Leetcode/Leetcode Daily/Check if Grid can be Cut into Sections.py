class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        len_rect = len(rectangles)
        cuts = [[0, 0] for _ in range(len_rect)]
        
        self.initializeCuts(rectangles, cuts, 1, 3)
        if self.isValidCut(cuts):
            return True

        self.initializeCuts(rectangles, cuts, 0, 2)
        return self.isValidCut(cuts)

    def initializeCuts(self, rectangles, cuts, xIdx, yIdx):
        for i in range(len(rectangles)):
            cuts[i][0] = rectangles[i][xIdx]
            cuts[i][1] = rectangles[i][yIdx]

    def isValidCut(self, cuts):
        n = len(cuts)
        x = 0
        j = 0
        
        cuts.sort(key=lambda a: (a[0], -a[1]))  # Sort by first element, and then second element in reverse order
        
        while j < n - 1:
            cur = cuts[j][1]
            while j < n and cuts[j][0] < cur:
                cur = max(cur, cuts[j][1])
                j += 1
            if j < n:
                x += 1
        
        return x >= 2

        