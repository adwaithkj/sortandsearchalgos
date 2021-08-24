class Solution:
    def checkifchild(self, root, p):
        if root:
            if root.val == p.val:
                return True
            if root.left and self.checkifchild(root.left, p):
                return True
            if root.right and self.checkifchild(root.right, p):
                return True
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        print("\n", p, q)
        print(self.checkifchild(root, p), self.checkifchild(root, q))
        if self.checkifchild(root, p) and self.checkifchild(root, q):

            temp1 = self.lowestCommonAncestor(root.left, p, q)
            temp2 = self.lowestCommonAncestor(root.right, p, q)

            if temp1 != None:
                return temp1
            if temp2 != None:
                return temp2

            return root

        return None
