# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        self.minheight=None
        def recursetree(root,height):
            if not root:
                return
            if self.minheight and height>self.minheight:
                return

            if root.left==None and root.right==None:
                if self.minheight==None:
                    self.minheight=height
                elif self.minheight>height:
                    self.minheight=height
                else:
                    pass
            else:
                recursetree(root.left,height+1)
                recursetree(root.right,height+1)

            
            

        recursetree(root,1)
        
        if self.minheight==None:
            print("none")
            return 1
        return self.minheight
