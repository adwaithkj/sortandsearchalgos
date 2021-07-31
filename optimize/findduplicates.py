# I have a very long string String str = "abcdefghiart----"
# Now I want to iterate over string and want to find the first
# duplicate character in string


def findduplicate(string):
    distinctwords = ""
    for i in string:
        if i not in distinctwords:
            distinctwords += i
        else:
            return i

    return None


print(findduplicate("abdveasdja"))
