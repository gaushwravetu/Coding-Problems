#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(n, arr, r):
    leftdict = defaultdict(int)
    leftdict[arr[0]]+=1
    rightdict = defaultdict(int)
    result = 0
    for i in range(1,n):
        rightdict[arr[i]]+=1
    for i in range(1,n):
        count1=0;count2=0;
        mid = arr[i]
        rightdict[mid]-=1
        right = mid*r
        left = mid//r
        if left in leftdict and mid%r==0:
            count1 = leftdict.get(left)
        if right in rightdict:
            count2 = rightdict.get(right)
        leftdict[mid]+=1
        # print(rightdict, leftdict)
        # print(count1,count2)
        result+=(count1*count2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(n, arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
