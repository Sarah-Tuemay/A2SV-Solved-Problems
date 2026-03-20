# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
        return self.traverse(p) == self.traverse(q)

    def traverse(self, root):
        if not root:
            return []
        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if type(node) == int or not node:
                res.append(node)
            else:
                stack.append(node.right)
                stack.append(node.left)
                stack.append(node.val)

        return res
