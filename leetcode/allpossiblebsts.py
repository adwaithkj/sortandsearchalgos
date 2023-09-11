
        

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int):
        rem=list(range(1,n+1))
        
        ans=[]
        length=len(rem)
        def recursetree(head,tail,rem,res):
            if rem==[]:
                ans.append(head)
                return None
            for i in range(len(rem)):
                newrem=rem[:]
                del newrem[i]
                
                if head==None or len(newrem)==length-1:
                    head=TreeNode(rem[i])
                    recursetree(head,head,newrem,res)
                else:
                    if rem[i]>tail.val:
                        tail.right=TreeNode(rem[i])
                        recursetree(head,tail.right,newrem,res)
                    else:
                        tail.left=TreeNode(rem[i])
                        recursetree(head,tail.left,newrem,res)
                    

        recursetree(None,None,rem,ans)

        return ans
p=Solution()
print(p.generateTrees(2))
                

                
                    
                        
            
                
        

