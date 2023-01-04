
res = []
d = {}
d[2] = "abc"
d[3] = "def"
d[4] = "ghi"
d[5] = "jkl"
d[6] = "mno"
d[7] = "pqrs"
d[8] = "tuv"
d[9] = "wxyz"


def recursetree(digits, arr=[]):
    if digits == []:
        return
    n = digits.pop(0)

    if arr == []:
        for i in d[int(n)]:
            arr.append(i)
    else:
        temp = []
        for i in range(len(arr)):
            for j in range(len(d[int(n)])):
                temp.append(arr[i]+d[int(n)][j])
        arr = temp

    if digits == []:
        res += arr

    else:
        recursetree(digits, arr)


recursetree(list("23"))
