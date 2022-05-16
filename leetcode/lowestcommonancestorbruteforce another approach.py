# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # let us first do level order traversal
        levelorder = []

        queue = []

        queue.append(root)

        while queue != []:
            node = queue.pop(0)
            levelorder.append(node)

            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

        for i in levelorder:
            if (self.checkif(i, p) and self.checkif(i, q)):
                out = i
        return out

    def checkif(self, ancestor, node):

        if ancestor == node:
            return True

        if ancestor.left != None and self.checkif(ancestor.left, node):
            return True
        if ancestor.right != None and self.checkif(ancestor.right, node):
            return True

        return False
