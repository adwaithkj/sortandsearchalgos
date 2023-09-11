# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        newtreehead=TreeNode()
        headpointer=newtreehead
        
        self.gr=100
        self.greater=0
        if root==None:
            return None
        def recursetree(root,ptr):

            if not root:
                return self.greater

            if root.right:
                ptr.right=TreeNode()
                newptr=ptr.right
                recursetree(root.right,newptr)
                
            # self.gr=root.val


            self.greater=self.greater+root.val

            ptr.val=self.greater

            if root.left:
                ptr.left=TreeNode()
                newptr=ptr.left
                recursetree(root.left,newptr)

        recursetree(root,headpointer)
        return newtreehead
                    
                    


            




            

        