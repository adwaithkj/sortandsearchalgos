class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out=[]
        print(root)
        print(out)
        if root!=None:
            print("have gotten in the print statement")
            out.extend(self.inorderTraversal(root.left))
            out.extend([root.val])
            out.extend(self.inorderTraversal(root.right))
        # else:
        #     out.append(None)
        print("second print of out",out)
        return out
        