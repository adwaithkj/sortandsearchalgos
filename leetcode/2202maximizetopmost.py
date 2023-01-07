class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        r = []
        if k == 0:
            return nums[0]
        if k == 1 and len(nums) >= 2:
            return nums[1]
        if len(nums) >= k:
            for i in range(k-1):
                r.append(nums.pop(0))
            if r != []:
                print(nums, r)
                if len(nums) > 1:
                    return max([nums[1], max(r)])
                else:
                    return max(r)

        else:
            if len(nums) == 1:
                if k % 2 == 1:
                    return -1
            return max(nums)
        return -1
