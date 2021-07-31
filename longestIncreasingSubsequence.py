def checkasc(arr):

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def LIS(arr, dict={}):
    if str(arr) in dict:
        return dict[str(arr)]

    print(arr)

    if checkasc(arr):
        print("This is strictly increasing")
        return len(arr)
    largest = None

    for i in range(len(arr)):
        newarr = arr[:]
        newarr.remove(arr[i])
        length = LIS(newarr)
        dict[str(newarr)] = length

        if largest == None or length > largest:
            largest = length

    return largest


if __name__ == "__main__":
    arr = [2, 4, 3, 7, 4, 5]

    # arr = [2, 1, 5, 2, 72, 3, 4, 5, 7, 32, 432, 432, 4, 324, 32, 43, 423, 43, 242, 34, 2, 134, 4, 325,
    #        435, 31, 231, 1245, 434, 2435, 4, 345, 2345234, 3, 4324, 34, 2, 3423, 42, 43, 24, 23, 423, 4, 3]

    print(LIS(arr))
