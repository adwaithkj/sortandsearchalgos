def checkadj(arr):
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return i-1
    return None


def superReducedString(s):

    s = list(s)
    print(checkadj(s))
    while s != [] and checkadj(s) != None:
        i = checkadj(s)
        print(s, i)
        s.remove(s[i])
        s.remove(s[i])
    if s == []:
        return "Empty String"
    return "".join(s)


if __name__ == "__main__":
    print(superReducedString(
        "zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh"))
