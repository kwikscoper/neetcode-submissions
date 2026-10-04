# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #first thought is to go level by level checking right to left
        
        if not root:
            return []
        
        level = 0
        output = []
        queue = deque([root])
        while queue:
            output.append(queue[0].val)
            for item in range(len(queue)):
                currNode = queue.popleft()
                if currNode.right:
                    queue.append(currNode.right)
                if currNode.left:
                    queue.append(currNode.left)            

        return output