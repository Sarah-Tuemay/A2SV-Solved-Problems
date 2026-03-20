# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val and self.isSameTree(node, subRoot):
                return True            
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return False

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

