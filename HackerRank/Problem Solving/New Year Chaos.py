#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict 
# Complete the minimumBribes function below.
def minimumBribes(n, q):
    count=0
    i = n-1
    while(i>=0):
        if(q[i]!=i+1):
            if i-1>=0 and q[i-1]==i+1:
                count+=1
                (q[i-1],q[i])=(q[i],q[i-1])
            elif(i-2>=0 and q[i-2]==i+1):
                count+=2
                (q[i-2],q[i-1])=(q[i-1],q[i-2])
                (q[i-1],q[i])=(q[i],q[i-1])
            else:
                print('Too chaotic')
                return
        i-=1
    print(count)




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(n, q)
