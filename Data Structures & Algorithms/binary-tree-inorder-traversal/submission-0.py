# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def recurse(root, res):
            if not root:
                return

            recurse(root.left, res)
            res.append(root.val)
            recurse(root.right, res)

        res = []
        recurse(root, res)
        return res