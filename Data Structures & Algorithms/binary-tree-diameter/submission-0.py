# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #at each split node, we need the length from there to root, and length from there to deepest leaf node

        self.maxPath = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.maxPath = max(self.maxPath, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.maxPath