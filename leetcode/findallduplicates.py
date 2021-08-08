# given that in the array each element is within  the bounds 1, len(n) find the duplicate elements with n time complexity and no extra space complexity

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        newarr = nums[:]
        stack = []
        for i in range(len(nums)):
            if newarr[nums[i]-1] != -1:
                newarr[nums[i]-1] = -1
            else:
                stack.append(nums[i])
        return stack
