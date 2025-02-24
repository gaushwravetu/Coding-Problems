class Solution:
    def mostProfitablePath(self, connections: List[List[int]], bob_start: int, node_values: List[int]) -> int:
         # Step 1: Build the tree as an adjacency list
        adjacency_list = defaultdict(list)
        for src, dest in connections:
            adjacency_list[src].append(dest)
            adjacency_list[dest].append(src)

        # Step 2: Find Bob's path from `bob_start` to `0`
        bob_visit_order = [-1] * len(node_values)
        bob_route = []

        def trace_bob_path(current, parent):
            if current == 0:
                return True
            for neighbor in adjacency_list[current]:
                if neighbor != parent:
                    bob_route.append(current)
                    if trace_bob_path(neighbor, current):
                        return True
                    bob_route.pop()
            return False

        trace_bob_path(bob_start, -1)
        for idx, node in enumerate(bob_route):
            bob_visit_order[node] = idx

        # Step 3: DFS to find Alice's max profit
        def compute_max_profit(current, parent, accumulated_profit, time_step):
            if bob_visit_order[current] == -1 or bob_visit_order[current] > time_step:
                accumulated_profit += node_values[current]
            elif bob_visit_order[current] == time_step:
                accumulated_profit += node_values[current] // 2

            # If leaf node (except root), return score
            if len(adjacency_list[current]) == 1 and current != 0:
                return accumulated_profit

            max_profit = float('-inf')
            for neighbor in adjacency_list[current]:
                if neighbor != parent:
                    max_profit = max(max_profit, compute_max_profit(neighbor, current, accumulated_profit, time_step + 1))

            return max_profit

        return compute_max_profit(0, -1, 0, 0)

        