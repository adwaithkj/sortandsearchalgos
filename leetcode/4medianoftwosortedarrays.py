class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted=[]
        length=len(nums1+nums2)

        flag= 0 if length%2==0 else 1

        while nums1+nums2!=[]:

            if nums1!=[] and nums2!=[] :
                if nums1[0]<nums2[0]:
                    sorted.append(nums1.pop(0))
                else:
                    sorted.append(nums2.pop(0))
            elif nums1==[]:
                sorted.append(nums2.pop(0))
                
            else :
                sorted.append(nums1.pop(0))
            
            if len(sorted)==length//2+1 and flag==1:
                return sorted[-1]
            if len(sorted)==length//2+1 and flag==0:
                return (sorted[-1]+sorted[-2])/2
            # print(sorted)
            
            
        
    
        


        