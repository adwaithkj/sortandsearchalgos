#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

# select any number of adjacent buildings


def findarea(h):
    smallest = h[0]
    for i in h:
        if i < smallest:
            smallest = i
    return smallest*(len(h)-1)


def largestRectangle(h):
    largestarea = 0

    for i in range(len(h)):
        for j in range(i+1, len(h)):
            p = findarea(h[i:j])
            if p > largestarea:
                largestarea = p

    return largestarea
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
