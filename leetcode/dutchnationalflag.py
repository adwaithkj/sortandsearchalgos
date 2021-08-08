def sortColors(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # we are going to use the dutch national flag algorithm to solve thois problem

    low = mid = 0
    high = len(nums)-1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


if __name__ == '__main__':
    arr = [1, 2, 0]
    sortColors(arr)
    print(arr)
