#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    (countz,countn,countp)=(0,0,0)
    for i in(arr):
        if(i==0):
            countz+=1
        elif(i>0):
            countp+=1
        elif(i<0):
            countn+=1
    return(format(countp/(countz+countp+countn),'.6f'),format(countn/(countz+countp+countn),'.6f'),format(countz/(countz+countp+countn),'.6f'))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in(plusMinus(arr)):
        print(i)
