#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
from collections import defaultdict
def countApplesAndOranges(s, t, a, b, apples, oranges):
    mydict = defaultdict(int)
    acount=0;ocount=0
    for i in range(s,t+1):
        mydict[i]+=1
    for i in range(len(apples)):
        tempapple = 0
        tempapple = apples[i]+a
        if(tempapple in mydict):
            acount+=1
    print(acount)
    for i in range(len(oranges)):
        temporange = 0
        temporange = oranges[i]+b
        if(temporange in mydict):
            ocount+=1
    print(ocount)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
