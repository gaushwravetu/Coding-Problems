#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(n,container):
    rowlist = []
    columnlist = []
    for i in range(n):
        rowsum=0;columnsum=0
        for j in range(n):
            rowsum+=container[i][j]
            columnsum+=container[j][i]
        rowlist.append(rowsum)
        columnlist.append(columnsum)
    rowlist.sort()
    columnlist.sort()
    if(rowlist==columnlist):
        return("Possible")
    else:
        return("Impossible")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(n,container)

        fptr.write(result + '\n')

    fptr.close()
