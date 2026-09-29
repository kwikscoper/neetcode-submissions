class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        def dfs(node):
            visited[node] = True
            for nextNode in adj[node]:
                if not visited[nextNode]:
                    dfs(nextNode)

        total_components = 0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                total_components += 1

        return total_components