class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        countlist = [0 for _ in range(n)]
        count=0
        for i in edges:
            countlist[i[1]]+=1
        # print(countlist)
        for i in range(n):
            if countlist[i] == 0:
                champion = i
                count+=1
            if count>1:
                return -1
        return champion


        