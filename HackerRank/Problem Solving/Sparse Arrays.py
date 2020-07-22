#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    stringdict = defaultdict(int)
    result=[]
    for i in strings:
        stringdict[i]+=1
    for j in queries:
        if j in stringdict:
            result.append(stringdict[j])
        else:
            result.append(0)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
