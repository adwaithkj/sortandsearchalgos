
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        node = root

        if p.val >= q.val:
            g = p
            l = q
        else:
            g = q
            l = p

        def recursetree(node):

            if g.val >= node.val and l.val <= node.val:
                return node

            if g.val > node.val and l.val > node.val:
                return recursetree(node.right)

            if g.val < node.val and l.val < node.val:
                return recursetree(node.left)

        return recursetree(node)
