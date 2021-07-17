# write a function canConstruct(target, wordBank) that accepts a targetstring and an array of strings.


# The function should return a boolean indicating whether or not the `targest ` can be constructed by concatenating the elements of the `wordBank` array.
# we can reuse the elements of the wordnank

def removeString(string1, string2):

    string1 = list(string1)
    string2 = list(string2)

    i = 0

    if string1[0] == string2[0]:

        while i < len(string1) and i < len(string2) and string1[i] == string2[i]:

            del string1[i]
            del string2[i]

        return "".join(string1)

    elif string1[-1] == string2[-1]:
        # print("gone into the print statement")
        while len(string1) >= 1 and len(string2) >= 1 and string1[-1] == string2[-1]:
            del string1[-1]
            del string2[-1]

        return "".join(string1)
    else:
        return False


def canConstruct(target, wordBank, dict1={}):
    if target in dict1:
        return dict1[target]

    if target == "":
        return True

    for i in wordBank:
        if removeString(target, i) != False:

            remainderTarget = removeString(target, i)
            if canConstruct(remainderTarget, wordBank):
                dict1[remainderTarget] = True
                return True
    dict1[target] = False
    return False


if __name__ == '__main__':
    # target = "abcdef"
    # wordBank = ["ab,abc,cd,def,abcd"]
    target = "hellofromtheotherside"
    wordBank = ["hello", "from", "the", "other", "side"]

    # print(removeString("abcde", "abc"))
    # print(removeString("somethinginetheway", "theway"))
    # print(removeString("something", "hello"))

    print(canConstruct(target, wordBank))
