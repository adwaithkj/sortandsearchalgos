#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    dict = {}
    for i in s:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    values = []

    for i in dict.values():
        values += [i]

    unique = []
    for i in values:
        if i not in unique:
            unique.append(i)

    print(dict, values, unique)
    if len(unique) == 1:
        return "YES"
    elif len(unique) > 2:
        return "NO"
    elif unique[0]-unique[1] == 1:
        return "YES"
    else:
        return "NO"
    # Write your code here


if __name__ == '__main__':

    s = "aabbcd"

    result = isValid(s)
    print(result)
