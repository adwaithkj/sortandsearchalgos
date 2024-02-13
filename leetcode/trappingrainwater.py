class Solution:
    def trap(self, height: List[int]) -> int:
        self.sum=0

        if len(set(height))==1:
            return 0
        a=0
            
        def recursetree(li):
            if len(li)==0:
                return None

            if len(li)>1 and li[0]>max(li[1:]):
                li[0]=max(li[1:])
                

            maxi=li[0]
            
            for i in range(len(li)-1):

                if li[i+1] >= maxi:
                    
                    recursetree(li[i+1:])
                    break
                
                self.sum+=maxi-li[i+1]
                # print(self.sum)

        recursetree(height)
        return self.sum

        