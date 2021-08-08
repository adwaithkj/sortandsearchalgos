def subsetsum(arr, targetsum):
    if targetsum == 0:
        return True
    if targetsum < 0:
        return False

    for i in arr:
        newarr = arr[:]
