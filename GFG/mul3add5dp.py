# 2) A number starting from 1 can be got by either multiplying 3 or adding 5 to it. Given a number, find the sequence of operations to get it or say it’s not possible.
# Eg: 13 = 1 * 3 + 5 + 5, 15 ; Not possible

def check(n):
    if n == 1 or n == 6:
        return True
    if n < 1:
        return False

    retvalue = []

    if n % 3 == 0:
        if check(n/3):

            return True
    if check(n-5):
        return True

    return False


if __name__ == '__main__':
    num = 11

    print(check(num))
