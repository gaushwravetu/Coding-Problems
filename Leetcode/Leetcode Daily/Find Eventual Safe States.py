class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        in_degree = [0] * n
        
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
            in_degree[u] = len(graph[u])
        
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        safe = set(queue)
        
        while queue:
            node = queue.popleft()
            for neighbor in reverse_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    safe.add(neighbor)
        
        return sorted(safe)
        