class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #if there is a cycle or we cannot reach all nodes it is not a valid tree
        #we can use dfs and if we ever hit a next node that we can seen before, it is a cycle

        if len(edges) > (n - 1):
            return False

        adj = [[] for node in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for nextNode in adj[node]:
                if nextNode != parent:
                    if not dfs(nextNode, node):
                        return False

            return True

        result = dfs(0, -1)
        if len(visited) != n:
            return False
        else:
            return result