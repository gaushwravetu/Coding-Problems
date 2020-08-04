#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(n, arr):
    result = []
    result.append(n)
    arr.sort()
    #print(arr)
    for i in range(len(arr)-1):
        if arr[i]==0:
            continue
        temp = arr[i]
        #print(arr[i])
        for j in range(i,len(arr)):
            if arr[j]-temp==0:
                arr[j]=arr[j]-temp
                n-=1
            else:
                arr[j]=arr[j]-temp
        #print(arr)
        if n!=0:
            result.append(n)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(n, arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
