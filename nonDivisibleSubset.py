#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#


def check(k, s):
    if len(s) == 1:
        if s[0] % k == 0:
            return True

    for i in range(len(s)):
        for j in range(i, len(s)):
            if (s[i]+s[j]) % k != 0:

                return False
    return True


def nonDivisibleSubset(k, s):

    if len(s) < 2:
        return None

    if check(k, s):
        return s

    largestCombination = None

    for i in s:
        newarr = s[:]
        newarr.remove(i)

        subset = nonDivisibleSubset(k, newarr)

        if subset != None:
            if largestCombination == None:
                largestCombination = subset
            elif len(largestCombination) < len(subset):
                largestCombination = subset

    if largestCombination != None:
        return len(largestCombination)

    # Write your code here


if __name__ == '__main__':

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # s = list(map(int, input().rstrip().split()))
    k = 2
    s = [1, 2, 4, 7]

    result = nonDivisibleSubset(k, s)
    print(result)
