# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        min_ = float('inf')
        def traverse(node):
            nonlocal min_
            if not node:
                return 0
            
            stack.append(node.val)
            traverse(node.left)
            traverse(node.right)

            if not node.right and not node.left:
                min_ = min(min_, len(stack))

            stack.pop()
            return min_
        
        return traverse(root)