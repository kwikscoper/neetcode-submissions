class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, parent):
            if node not in visited:
                visited.add(node)
                for nextNode in adj[node]:
                    dfs(nextNode, node)

        total_components = 0
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                total_components += 1

        return total_components