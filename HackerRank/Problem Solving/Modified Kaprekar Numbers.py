#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    keprekarlist = []
    for i in range(p,q+1):
        if(i>3):
            kepsq = str(i**2)
            j = len(str(i))
            keplen = len(kepsq)
            #print(i,kepsq,len(kepsq),j)
            if(len(kepsq)>2):
                checksum = int(kepsq[:keplen-j])+int(kepsq[keplen-j:])
            else:
                checksum = int(kepsq[0])+int(kepsq[1])
            #print(int(kepsq[:j]),int(kepsq[j-1:]))
            if(int(i)==checksum):
                keprekarlist.append(i)
        elif(i==1):
            keprekarlist.append(1)
    if(len(keprekarlist)!=0):
        print(*keprekarlist)
    else:
        print("INVALID RANGE")





if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
