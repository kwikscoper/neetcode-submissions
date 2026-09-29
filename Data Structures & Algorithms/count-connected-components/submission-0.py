class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodeSet = set(range(n))

        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, parent):
            if node not in visited:
                visited.add(node)
                nodeSet.discard(node)
                for nextNode in adj[node]:
                    if nextNode != parent:
                        dfs(nextNode, node)

        total_components = 0
        while nodeSet:
            dfs(next(iter(nodeSet)), -1)
            total_components += 1

        return total_components