#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sumXor function below.
def sumXor(n):
    if n==0:
        return 1
    else:
        mystr = "{0:b}".format(n)
        mydict = Counter(mystr)
        result = mydict.get('0')
        if(result==None):
            return 1
        else:
            return 2**result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
