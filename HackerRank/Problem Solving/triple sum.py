#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
from collections import defaultdict

# Complete the triplets function below.
def triplets(a, b, c):
    # count=0
    # mydict = defaultdict(int)
    # for r in itertools.product(a,b,c):
    #     if r[1]>=r[0] and r[1]>=r[2]:
    #         if r not in mydict:
    #             mydict[r]+=1
    #             count+=1
    #             #print(r)
    # print(mydict)
    count = 0
    mydictA = defaultdict(int)
    mydictC = defaultdict(int)
    mydictB = defaultdict(int)
    for h in b:
        mydictB[h]+=1
    for i in a:
        mydictA[i]+=1
    for j in c:
        mydictC[j]+=1
    for k in mydictB:
        countA=0;countC=0
        for x in mydictA:
            if x<=k:
                countA+=1
        for y in mydictC:
            if y<=k:
                countC+=1
        print(countA,countC)
        count+=countA*countC
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
