#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    allpoint=0;bobpoint=0
    for i in range(3):
        if(a[i]>b[i]):
            allpoint+=1
        elif(a[i]<b[i]):
            bobpoint+=1
    return(allpoint,bobpoint)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
