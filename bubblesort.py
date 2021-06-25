def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubblesort(arr):
    flag = 1

    while flag == 1:
        flag = 0
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                swap(arr, i, i+1)
                flag = 1


if __name__ == "__main__":

    arr = [12, 11, 13, 5, 6, 7]

    print(f"Given array is: {arr}", end="\n")

    bubblesort(arr)

    print(f"Sorted array is: {arr}", end="\n")
