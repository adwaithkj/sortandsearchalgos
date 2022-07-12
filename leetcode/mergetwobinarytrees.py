class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        root = TreeNode(None)
        node1 = root1
        node2 = root2

        def recursetree(node1, node2, root):

            if not node1 and not node2:
                return root
            if node1 and not node2:
                if not root:
                    root = TreeNode()
                root.val = node1.val
                print(root.val)

                root.left = recursetree(node1.left, node2, root.left)
                root.right = recursetree(node1.right, node2, root.right)
                return root

            if node2 and not node1:
                if not root:
                    root = TreeNode()

                root.val = node2.val
                print(root.val)

                root.left = recursetree(node1, node2.left, root.left)
                root.right = recursetree(node1, node2.right, root.right)
                return root
            if node1 and node2:
                root = TreeNode()

                root.val = node1.val+node2.val
                print(root.val)

                root.left = recursetree(node1.left, node2.left, root.left)
                root.right = recursetree(node1.right, node2.right, root.right)
                return root

        root = recursetree(node1, node2, root)

        if root.val == None:
            return None
        return root
