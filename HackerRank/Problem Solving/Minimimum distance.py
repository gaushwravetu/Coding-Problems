#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the minimumDistances function below.
def minimumDistances(n, a):
    mydict = defaultdict(list)
    mymin = 9999
    flag = False
    for i in range(n):
        mydict[a[i]].append(i+1)
    for i in mydict:
        if len(mydict[i])==2:
            result = mydict[i][1]-mydict[i][0]
            print(result)
            mymin = min(result,mymin)
            flag = True
    if flag:
        return mymin
    else:
        return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(n, a)

    fptr.write(str(result) + '\n')

    fptr.close()
