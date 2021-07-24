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

    print(LIS(arr))
