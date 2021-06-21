def binarysearch(arr, x):
    Found = False
    length = len(arr)
    m = 0
    n = length-1

    while True:
        p = int((m+n)/2)

        if arr[p] == x:
            return p
        elif m+1 == n:
            return False

        elif arr[p] > x:
            n = p

        else:
            m = p


def main():
    arr = input("enter sorted data with spaces : ")
    arr = list(map(int, arr.strip().split(' ')))

    x = int(input("enter the number to search for in the list : "))

    if binarysearch(arr, x) != False:
        print(f"the number is found at index {binarysearch(arr,x)}")
    else:
        print("the number is not found in the list :(")


main()
