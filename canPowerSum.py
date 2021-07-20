import math
import os
import random
import re
import sys


def powerSum(X, N, rangelist):
    lists = []
    if X == 0:
        return []
    if X < 0:
        return None

    if rangelist == None:
        return None

    if rangelist != None:
        for i in rangelist:
            newrange = rangelist[:]
            newrange.remove(i)
            remainder = X-i**N
            newlist = powerSum(remainder, N, newrange)

            if newlist != None:
                return (newlist+[i])
    return None


    # Write your code here
if __name__ == '__main__':

    # X = int(input().strip())

    # N = int(input().strip())
    X = 19
    N = 2

    rangelist = list(range(1, math.ceil(X**(1/N))))

    result = powerSum(X, N, rangelist)

    print(result)
