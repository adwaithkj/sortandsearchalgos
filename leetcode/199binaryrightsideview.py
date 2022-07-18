# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):

        head = root
        output = []
        olevel = []

        if root == None:
            return []

        def recursetree(node, level):
            if level not in olevel:
                output.append(node.val)
                olevel.append(level)

            if node.right:
                recursetree(node.right, level+1)
            if node.left:
                recursetree(node.left, level+1)

        recursetree(head, 0)

        return output
