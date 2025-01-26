#Maximum Employees to Be Invited to a Meeting

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_degree = [0] * n
        graph = defaultdict(list)
        reverse_graph = defaultdict(list)

        # Building the graph and in-degree array
        for i, f in enumerate(favorite):
            graph[i].append(f)
            reverse_graph[f].append(i)
            in_degree[f] += 1

        # Topological sort using BFS to compute chain lengths
        queue = deque()
        chain_length = [0] * n
        visited = [False] * n

        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            visited[node] = True
            for neighbor in graph[node]:
                chain_length[neighbor] = max(chain_length[neighbor], chain_length[node] + 1)
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # DFS for cycle detection
        def dfs(node, depth, stack_map):
            if visited[node]:
                return 0
            if node in stack_map:
                return depth - stack_map[node]
            stack_map[node] = depth
            result = dfs(favorite[node], depth + 1, stack_map)
            stack_map.pop(node)
            visited[node] = True
            return result

        max_cycle_length = 0
        for i in range(n):
            if not visited[i]:
                max_cycle_length = max(max_cycle_length, dfs(i, 0, {}))

        # Calculating contribution from mutual favorite pairs
        mutual_favorites_sum = 0
        for i in range(n):
            if favorite[favorite[i]] == i and i < favorite[i]:
                mutual_favorites_sum += 2 + chain_length[i] + chain_length[favorite[i]]

        return max(max_cycle_length, mutual_favorites_sum)
        