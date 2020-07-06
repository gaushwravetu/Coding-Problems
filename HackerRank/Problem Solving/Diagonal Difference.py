#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(n,arr):
    (sumdig1,sumdig2) = (0,0)
    for i in range(n):
       sumdig1+=arr[i][i]
       sumdig2+=arr[i][n-1-i]
    return(abs(sumdig1-sumdig2))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(n,arr)

    fptr.write(str(result) + '\n')

    fptr.close()
