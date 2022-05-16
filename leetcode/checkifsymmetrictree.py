
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def recursetree(left, right):

            if left and not right:
                return False
            if right and not left:
                return False

            if not left and not right:
                return True

            if left.val != right.val:
                return False

            return recursetree(left.left, right.right) and recursetree(left.right, right.left)

        return recursetree(root.left, root.right)
