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


def powerSum(X, N,i = 1):
    count =0
    # Write your code here
    if(X == 0):
        # return count+1
        return 1
    
    if(X < pow(i,N)):
        return 0
    
    while pow(i,N) <= X:
        res = powerSum(X-pow(i,N),N,i+1)
        count+=res
        # if(res!=count):
        #     return count+res
            
        
        i+=1
       
    return count
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
