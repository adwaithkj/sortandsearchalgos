def howSum(targetSum, arr, dict1):
    if targetSum in dict1:
        return dict1[targetSum]
    if targetSum < 0:

        return None

    if targetSum == 0:

        return []

    for i in arr:
        sum = targetSum-i
        p = howSum(sum, arr, dict1)

        if p != None:
            list1 = [i]
            dict1[targetSum] = p+list1
            return p+list1
    targetSum = None
    return None


targetSum = int(input("Enter the Target Sum =>"))

arr = (input("Enter the array list seperated by spaces=>"))
arr = arr.strip().split(" ")

arr = list(map(int, (arr)))
print(f" The entered list is {arr} and the target sum is {targetSum}")


# targetSum = 110

# arr = [7, 1, 2, 3, 4, 5]

# targetSum = 8
# arr = [9, 2, 3, 5]

dict1 = {}
print(howSum(targetSum, arr, dict1))

# time complexity of this problem
# m=target Sum
# n=arr length

# Brute force
#time= O(n^m *m)
# space=O(n)

# memoized
#time= O(m*n)
# space=O(m*n) cause the main cause of space is coming from the dictionary which at worst will store m keys and each value will be at most the whole array
