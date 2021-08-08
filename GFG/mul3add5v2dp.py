# 2) A number starting from 1 can be got by either multiplying 3 or adding 5 to it. Given a number, find the sequence of operations to get it or say it’s not possible.
# Eg: 13 = 1 * 3 + 5 + 5, 15 ; Not possible

def check(n):
    retvalue = []
    if n == 1:
        return retvalue
    if n < 1:
        return None
    retvalue.append(n)

    if n % 3 == 0:
        temp = check(n//3)
        if temp != None:
            retvalue.extend(temp)
            return retvalue

    temp = check(n-5)
    if temp != None:
        retvalue.extend(temp)
        return retvalue

    return None


if __name__ == '__main__':
    num = 13

    print(check(num)+[1])
