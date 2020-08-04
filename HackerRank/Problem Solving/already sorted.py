#!/bin/python3

import math
import os
import random
import re
import sys
import copy
def almostSorted(n, arr):
    sortedarry = copy.deepcopy(arr)
    sortedarry.sort()
    if sortedarry==arr:
        print('yes')
        return
    left=right=-1
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            left=i
            break
    for j in range(n-1,0,-1):
        if arr[j]<arr[j-1]:
            right=j
            break
    temp = copy.deepcopy(arr)
    temp[left],temp[right]=temp[right],temp[left]
    if temp==sortedarry:
        print('yes')
        print("swap",left+1,right+1)
        return
    temp = copy.deepcopy(arr)
    #print(temp,left,right)
    temp = arr[:left]+arr[left:right+1][::-1]+temp[right+1:]
    #print(temp)
    if temp==sortedarry:
        print('yes')
        print('reverse', left+1, right+1)
        return
    print('no')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(n, arr)
