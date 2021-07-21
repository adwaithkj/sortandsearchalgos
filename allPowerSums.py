
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#


def powerSum(X, N, rangelist, path=[], dict1={}):

    if X in dict1:
        return dict1[X]

    if X == 0:
        # print(path)
        return [path]
    if X < 0:
        return None
    paths = []

    for i in rangelist:
        sendPath = path[:]
        sendPath += [i]
        remainder = X-i**N
        newRange = rangelist[:]
        newRange.remove(i)
        # print("The remainder ,n ,rangelist,path are the following",
        #       remainder, N, newRange, sendPath)

        newPath = powerSum(remainder, N, newRange, sendPath, dict1)

        if newPath != None:
            dict1[X] = newPath
            for q in newPath:
                paths.append(q)

            # return paths

        # return newPath
        # for z in newPath:
        #     paths.append(z)

    dict1[X] = paths
    return paths

    # Write your code here
if __name__ == '__main__':

    # X = int(input().strip())

    # N = int(input().strip())
    X = 400
    N = 2

    rangelist = list(range(1, math.ceil(X**(1/N))+1))

    result = powerSum(X, N, rangelist)

    for i in range(len(result)):
        result[i].sort()

    list2 = []
    for i in result:
        if i not in list2:
            list2.append(i)
    print(list2)


# Find the number of ways that a given integer, , can be expressed as the sum of the

# powers of unique, natural numbers.

# For example, if
# and , we have to find all combinations of unique squares adding up to . The only solution is

# .

# Function Description

# Complete the powerSum function in the editor below. It should return an integer that represents the number of possible combinations.

# powerSum has the following parameter(s):

#     X: the integer to sum to
#     N: the integer power to raise numbers to

# Input Format

# The first line contains an integer
# .
# The second line contains an integer

# .

# Constraints

# Output Format

# Output a single integer, the number of possible combinations caclulated.

# Sample Input 0

# 10
# 2

# Sample Output 0

# 1

# Explanation 0

# If
# and , we need to find the number of ways that

# can be represented as the sum of squares of unique numbers.

# This is the only way in which

# can be expressed as the sum of unique squares.

# Sample Input 1

# 100
# 2

# Sample Output 1

# 3

# Explanation 1

# Sample Input 2

# 100
# 3

# Sample Output 2

# 1

# Explanation 2

# can be expressed as the sum of the cubes of .
# . There is no other way to express as the sum of cubes.
