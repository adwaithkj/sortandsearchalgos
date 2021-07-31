def findsum(arr):
    sum = 0

    for i in range(len(arr)):
        if i % 2 == 0:
            sum += arr[i]
        else:
            sum -= arr[i]
    return sum


def findbestsum(arr, largest=0):
    if len(arr) == 1:
        if arr[0] > largest:
            return arr[0]
        else:
            return largest

    for i in arr:
        newarr = arr[:]
        newarr.remove(i)
        thissum = findsum(arr)
        nextsum = findbestsum(newarr, largest)
        if nextsum > largest:
            largest = nextsum
        elif thissum > largest:
            largest = thissum

    return largest


if __name__ == '__main__':
    print(findbestsum([1, 3, 4, 5]))
