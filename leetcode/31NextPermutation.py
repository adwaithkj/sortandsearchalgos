class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=nums[-1];
        breakpoint=-1
        for i in range(len(nums)-2,-1,-1):
            flag=(nums[i]>=temp)
            print(i,nums[i],temp)
            if flag==False:                
                for j in range(len(nums)-1,i,-1):
                    if nums[j]>nums[i]:
                        repl=j
                        break
                print(j)
                temp1=nums[i]
                nums[i]=nums[j]
                nums[j]=temp1
                breakpoint=i
                break
            temp=nums[i]
        if (breakpoint==-1):
            ret=nums[:]
            ret.reverse()
        else:
            ret=nums[:i+1]+sorted(nums[i+1:])
            print(nums[:breakpoint+1],nums[breakpoint+1:])
            print(ret)
        for i in range(len(nums)):
            nums[i]=ret[i]
        
        