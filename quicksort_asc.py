def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def quicksort(arr):

    if len(arr) > 1:
        pivot = arr[0]
        i = 1
        j = 0
        p = []
        q = []

        while i < len(arr):

            if arr[i] > pivot:
                p.append(i)
            i += 1

        while j < len(arr):

            if arr[-j] < pivot:
                q.append(j)
            j += 1

        k = 0
        while k < len(p) and k < len(q) and p[k]+q[k] < len(arr):
            swap(arr, p[k], q[k])
            k += 1

        arr = arr[1:]
        arr.insert[p[k], pivot]

        l = arr[:k]
        r = arr[k+1:]
        quicksort(l)
        quicksort(r)

        # position of the value of pivot will be  p[k]


if __name__ == "__main__":
    print("Welcome to yet another program written using the DAC 'Divide and Conquer ' paradigm ,\n quick sort. Although the name suggests quickness, the algorithm itself isn't as quick as it may sound.")

    arr = [12, 11, 13, 5, 6, 7]

    # arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]

    print(f"The unsorted array is {arr}")

    quicksort(arr)

    print(f"The sorted arr is {arr}")


# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     print("Given array is", end="\n")

#     quicksort(arr)
#     print("Sorted array is: ", end="\n")
