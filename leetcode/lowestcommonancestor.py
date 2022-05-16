# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.lca = 0

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recursetree(node):
            left = False
            right = False

            if not node:
                return False

            left = recursetree(node.left)

            right = recursetree(node.right)

            mid = (node == p or node == q)

            if mid + left + right >= 2:
                self.lca = node

            return mid or left or right

        recursetree(root)

        return self.lca
