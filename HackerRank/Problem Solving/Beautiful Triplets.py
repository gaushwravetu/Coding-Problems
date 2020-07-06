#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, a, n):
    count = 0
    #l1 = []
    for i in range(n-1):
        flag = False
        for j in range(i+1,n):
            if(a[j]-a[i]==d and not flag):
                flag=True
            elif(a[j]-a[i]==2*d and flag):
                count+=1
                break
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
