#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def encryption(s):
    s = list(s)
    for i in s:
        if i == " ":
            s.remove(i)
    length = len(s)
    rows = math.floor(length**(1/2))
    columns = math.ceil(length**(1/2))

    k = 0
    grid = []

    for i in range(rows):
        temp = []
        for j in range(columns):
            if k < len(s):
                temp.append(s[k])
                k += 1
        grid.append(temp)

    temp = []
    tgrid = []

    print(rows)
    print(columns)

    for i in range(columns):
        temp = []
        for j in range(rows):
            temp.append(0)
        tgrid.append(temp)

    for i in range(rows):
        for j in range(columns):
            try:
                tgrid[j][i] = grid[i][j]
            except:
                pass
    string = ""
    for i in range(columns):
        for j in range(rows):
            if tgrid[i][j] == 0:
                continue

            string += tgrid[i][j]
        string += " "
    return string

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
