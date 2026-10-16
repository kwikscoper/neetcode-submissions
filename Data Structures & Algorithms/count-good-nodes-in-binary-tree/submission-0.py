# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        stack = [(root, float('-inf'))]

        while stack:
            node, max_in_path = stack.pop()
            if not node:
                continue
            
            if node.val >= max_in_path:
                total += 1

            new_max = max(max_in_path, node.val)
            stack.append((node.right, new_max))
            stack.append((node.left, new_max))

        return total