class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        reachable = [set() for _ in range(n)]
        
        def dfs(course):
            if reachable[course]:
                return reachable[course]
            for neighbor in graph[course]:
                reachable[course].add(neighbor)
                reachable[course].update(dfs(neighbor))
            return reachable[course]

        for course in range(n):
            dfs(course)
        
        return [v in reachable[u] for u, v in queries]
        