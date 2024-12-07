from collections import defaultdict, deque
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        # Step 2: Find the starting node
        start_node = pairs[0][0]  # Default start node
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break

        # Step 3: Perform Hierholzer’s algorithm to find the Eulerian path
        def dfs(node):
            while graph[node]:
                next_node = graph[node].popleft()
                dfs(next_node)
                path.append((node, next_node))

        path = []
        dfs(start_node)
        path.reverse()  # Reverse to get the correct order

        return path
        