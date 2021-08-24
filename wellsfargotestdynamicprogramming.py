def possibilities(targetsum, length, sum=0, sumlength=0):

    if targetsum == sum and length == sumlength:
        return 1

    if sumlength > length:
        return 0

    return possibilities(targetsum, length, sum + 1, sumlength + 1) + possibilities(targetsum, length, sum-1, sumlength+1)


if __name__ == "__main__":
    targetsum = 0
    sum = 4

    print(possibilities(targetsum, sum))
