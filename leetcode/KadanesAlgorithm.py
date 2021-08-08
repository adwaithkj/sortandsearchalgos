class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max = nums[0]
        for i in nums:
            if sum >= 0:
                sum += i

            if sum > max:
                max = sum
            if sum < 0:
                sum = 0

        return max
