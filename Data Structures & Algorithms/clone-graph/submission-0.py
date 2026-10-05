"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}
        oldToNew[node] = Node(node.val)
        
        queue = deque([node])
        while queue:
            currNode = queue.popleft()
            for nextNode in currNode.neighbors:
                if nextNode not in oldToNew:
                    queue.append(nextNode)
                    oldToNew[nextNode] = Node(nextNode.val)
                oldToNew[currNode].neighbors.append(oldToNew[nextNode])

        return oldToNew[node]
            