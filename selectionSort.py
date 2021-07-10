def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selectionSort(arr):

    for i in range(len(arr)):
        smallest = arr[i]

        for j in range(i+1, len(arr)):
            print(i)

            if smallest > arr[j]:
                print(f"replacing {j} th position with {i}th position")
                swap(arr, j, i)
                smallest = arr[i]

            else:
                print('This is the smallest')
    return arr


# Driver code
array = [10, 7, 8, 9, 1, 5]

print(f'Given array: {array}')

selectionSort(array)

print(f'Sorted array: {array}')
