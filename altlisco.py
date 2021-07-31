
import sys

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

sys.setrecursionlimit(10**6)


def checkasc(arr):

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def LIS(arr, lists=[]):
    if len(arr) == 1:
        return arr

    for i in range(1, len(arr)):

        if LIS(arr[i:]) != None:
            combination = [arr[0]]+LIS(arr[i:], lists)
            if checkasc(combination) == True:
                lists.append(combination)
                return combination

            # for i in combination:
            #     lists.append(i)

    return None


if __name__ == "__main__":

    arr = [5, 1, 3, 4, 6, 2, 8]
    lists = []
    # n = input("enter the value of k for the kth smallest element")
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    print(LIS(arr, lists))
    print(lists)
