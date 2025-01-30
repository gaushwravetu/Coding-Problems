Divide Nodes Into the Maximum Number of Groups
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = {}
        components = []

        def bfs_check_bipartite(start):
            queue = deque([(start, 0)])
            visited[start] = 0
            component = [start]

            while queue:
                node, color = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited[neighbor] = 1 - color
                        queue.append((neighbor, 1 - color))
                        component.append(neighbor)
                    elif visited[neighbor] == color:
                        return None
            
            return component

        for node in range(1, n + 1):
            if node not in visited:
                component = bfs_check_bipartite(node)
                if component is None:
                    return -1
                components.append(component)
        def bfs_longest_path(start):
            queue = deque([start])
            dist = {start: 0}
            max_depth = 0

            while queue:
                node = queue.popleft()
                max_depth = max(max_depth, dist[node])
                for neighbor in graph[node]:
                    if neighbor not in dist:
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)

            return max_depth

        max_groups = 0
        for component in components:
            longest_path = 0
            for node in component:
                longest_path = max(longest_path, bfs_longest_path(node))
            max_groups += longest_path + 1

        return max_groups
        