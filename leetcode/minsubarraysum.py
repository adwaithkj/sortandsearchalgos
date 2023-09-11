class Solution:
    def minSubArrayLen(self, target,nums) :

        start=0
        end =len(nums)

        diff=[]
        

        def recursetree(start,end):
            if sum(nums[start:end])==target:
                diff.append(end-start)
            elif sum(nums[start:end])>=target:
                recursetree(start+1,end)
                recursetree(start,end-1)
            else:
                return
        if diff==[]:
            return 0
        return min(diff)


s=Solution()

print(s.minSubArrayLen(4,[1,4,4]))
        


        # now we have to find which is lesser than number

        
            

