# from sortedcontainers import SortedDict
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # mydict = SortedDict()
        # result = 0
        # for i in classes:
        #     if (i[0],i[1]) in mydict:
        #         mydict[(i[0],i[1])]+=1
        #     else:
        #         mydict[(i[0],i[1])]=1
        # for i in mydict:
        #     print(i)

        # Implementing using min-heap
        max_heap = []
        total_pass_ratio = 0

        for passi, totali in classes:
            current_ratio = passi / totali
            gain = ((passi + 1) / (totali + 1)) - current_ratio
            heapq.heappush(max_heap, (-gain, passi, totali))
            total_pass_ratio += current_ratio

        for _ in range(extraStudents):
            neg_gain, passi, totali = heapq.heappop(max_heap)
            gain = -neg_gain
            new_pass_ratio = (passi + 1) / (totali + 1)
            total_pass_ratio -= passi / totali
            total_pass_ratio += new_pass_ratio
            new_gain = ((passi + 2) / (totali + 2)) - new_pass_ratio
            heapq.heappush(max_heap, (-new_gain, passi + 1, totali + 1))

        return total_pass_ratio / len(classes)
            




        