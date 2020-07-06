#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minsum = arr[0]+arr[1]+arr[2]+arr[3]
    maxsum = arr[4]+arr[1]+arr[2]+arr[3]
    print(minsum,maxsum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    arr.sort()
    miniMaxSum(arr)

