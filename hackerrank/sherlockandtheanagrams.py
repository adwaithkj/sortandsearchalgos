# Two strings are anagrams of each other if the letters of one string
# can be rearranged to form the other string. Given a string, find the
# number of pairs of substrings of the string that are anagrams of each
# other.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def checkanagram(string1, string2):
    string1 = list(string1)
    string2 = list(string2)

    for i in string1:
        try:
            string2.remove(i)
        except:
            return False

    if string2 == []:
        return True
    else:
        return False


def sherlockAndAnagrams(s):
    s = list(s)
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            substrings.append(substring)
    print(substrings)
    sum = 0
    for i in range(len(substrings)):
        for j in range(i+1, len(substrings)):
            if checkanagram(substrings[i], substrings[j]):
                sum += 1
    return sum
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
