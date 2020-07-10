#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    clouds = len(c)
    i = 0;count=0
    if(clouds==2):
        if c[1]==0:
            return 1
        else:
            return 0

    while(i<clouds-2):
        if c[i+1]==1 or c[i+1]==0 and c[i+2]==0:
            i+=2
            count+=1
            if i+2==clouds:
                if c[i+1]==0:
                    count+=1
        elif c[i+1]==0:
            i+=1
            count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
