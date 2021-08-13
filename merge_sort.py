def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]

        mergesort(l)
        mergesort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]

                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


if __name__ == "__main__":
    print("welcome to the program")


arr = input("enter the list of numbers you want to get sorted with merge sort ")

arr = list(map(int, arr.strip().split(" ")))


print(f"the entered unsorted array is {arr}")

mergesort(arr)


print(f"The sorted array is {arr}")
