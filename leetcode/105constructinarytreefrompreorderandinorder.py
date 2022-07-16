# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        x = preorder[0]
        index = inorder.index(x)
        i = 0

        left = inorder[:index]
        right = inorder[index+1:]
        i += 1

        root = TreeNode(x)

        self.total = 1

        def recursetree(left, right, node):

            print(left, right, node)

            maxvalleft = None
            maxvalright = None

            for i in left:
                if maxvalleft == None or preorder.index(maxvalleft) > preorder.index(i):
                    maxvalleft = i

            for i in right:
                if maxvalright == None or preorder.index(maxvalright) > preorder.index(i):
                    maxvalright = i

            if maxvalleft:
                node.left = TreeNode(maxvalleft)
                newleft = left[:left.index(maxvalleft)]
                newright = left[left.index(maxvalleft)+1:]
                recursetree(newleft, newright, node.left)

            if maxvalright:
                node.right = TreeNode(maxvalright)
                newleft = right[:right.index(maxvalright)]
                newright = right[right.index(maxvalright)+1:]
                recursetree(newleft, newright, node.right)

        recursetree(left, right, root)
        print(root)
        return root
