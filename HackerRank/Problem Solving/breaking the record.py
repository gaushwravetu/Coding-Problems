#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    match = len(scores)
    if(match==1):
        return(0,0)
    win=0;lose=0
    tempmax=0;tempmin=0
    if scores[0]>scores[1]:
        tempmax=scores[0]
        tempmin = scores[1]
        lose+=1
    elif scores[1]>scores[0]:
        tempmin=scores[0]
        tempmax=scores[1]
        win+=1
    else:
        tempmin=scores[0]
        tempmax=scores[0]
    #print(tempmax,tempmin)
    for i in range(2,match):
        if tempmax<scores[i]:
            win+=1
            tempmax=scores[i]
        elif tempmin>scores[i]:
            lose+=1
            tempmin=scores[i]
    return(win,lose)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
