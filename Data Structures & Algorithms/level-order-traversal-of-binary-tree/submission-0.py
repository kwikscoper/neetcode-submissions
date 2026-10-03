# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #use bfs
        if not root:
            return []

        output = []
        queue = deque([root])
        visited = set()
        while queue:
            level_len = len(queue)
            output.append([])
            for item in range(level_len):
                currNode = queue.popleft()
                output[-1].append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)

        return output