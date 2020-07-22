#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    mydict = defaultdict(int)
    mymax = 0
    result=0
    for i in a:
        mydict[i]+=1
    print(mydict)
    # while(i<mydict-1):
    #     if i+1 in mydict:
    #         result = mydict.get(i)*mydict.get(i+1)
    #         mymax = max(mymax,result)
    for i in mydict:
        if i in mydict and i+1 in mydict:
            result = mydict[i]+mydict[i+1]
        mymax = max(mymax,result,mydict[i])
    return(mymax)
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
