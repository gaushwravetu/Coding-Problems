#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, m, queries):
    arrlist = [0]*(n+2)
    for i in range(m):
        arrlist[queries[i][0]]+=queries[i][2]
        arrlist[queries[i][1]+1]-=queries[i][2]
    #print(arrlist)
    result = 0;mymax=0
    for i in range(n+2):
        result+=arrlist[i]
        mymax = max(mymax,result)
    #print(arrlist)
    return(mymax)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, m, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
