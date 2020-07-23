#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(n, a, d):
    newlist = [0]*n
    for i in range(n):
        newindex = (i+(n-d))%n
        newlist[newindex] = a[i]
    return newlist
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(n, a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
