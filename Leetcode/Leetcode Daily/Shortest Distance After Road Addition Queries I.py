from collections import defaultdict, deque
from typing import List
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # result = []
        # def bfs(start,adj_list,n):
        #     visited = set()
        #     queue = deque([start])
        #     level = 0
        #     while(queue):
        #         node = queue.popleft()
        #         if node not in visited:
        #             visited.add(node)
        #             if node == n-1:
        #                 return level
        #             for neighbor in adj_list[node]:
        #                 queue.append(neighbor)
        #             # print(queue)
        #             level+=1
        #     return -1

        # # creating an adjacency list to store the value of the visited nodes u->v
        # adj_list = defaultdict(list)
        # for i in range(n-1):
        #     adj_list[i].append(i+1)
        # for j in queries:
        #     adj_list[j[0]].append(j[1])
        #     result.append(bfs(0,adj_list,n))
        # return result

        def bfs(start, end, graph):
            visited = [False] * n
            queue = deque([(start, 0)])  # (current_node, current_distance)
            
            while queue:
                node, dist = queue.popleft()
                if node == end:
                    return dist
                
                if not visited[node]:
                    visited[node] = True
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            queue.append((neighbor, dist + 1))
            return -1  # if no path exists
        
        # Create the initial graph with default roads
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        result = []
        for u, v in queries:
            graph[u].append(v)
            result.append(bfs(0, n - 1, graph))  # Calculate shortest path after each query
        
        return result




        