#!/bin/python3

import math
import os
import random
import re
import sys
def binsearch(alice,result):
    l = 0
    h = len(result)-1
    while(l<=h):
        mid = l+((h-l)//2)
        if(mid==alice):
            return mid
        elif(result[mid]<alice and alice<result[mid-1]):
            return mid
        elif(result[mid]>alice and alice>=result[mid+1]):
            return mid+1
        elif(result[mid]<alice):
            h = mid-1
        elif(result[mid]>alice):
            l = mid+1
    return -1
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice, scores_count, alice_count):
    result = [0]*(scores_count)
    result[0]=1
    res = [0]*(alice_count)
    for i in range(1,scores_count):
        if(scores[i]==scores[i-1]):
            result[i]=result[i-1]
        else:
            result[i] = result[i-1]+1
    print(result)
    for i in range(alice_count):
        if alice[i]>scores[0]:
            res[i] = 1
        elif alice[i]<scores[scores_count-1]:
            res[i] = result[scores_count-1]+1
        else:
            index = binsearch(alice[i],scores)
            res[i] = result[index]
            #print(index)
    #print(res)
    return res    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice, scores_count, alice_count)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
