def LIS(arr, lists=[]):
    if len(arr) == 1:
        return arr

    for i in range(1, len(arr)):
        if arr[i] > arr[0]:
            if LIS(arr[i:]) != None:
                combination = [arr[0]]+LIS(arr[i:])

                for i in combination:
                    lists.append(i)

    return combination


if __name__ == "__main__":

    arr = [2, 1, 4, 3, 4, 5]

    lists = []
    print(LIS(arr, lists))
