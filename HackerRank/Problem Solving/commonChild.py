#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the commonChild function below.
def commonChild(s1, s2, p, q, mat):
    for i in range(1,p+1):
        for j in range(1,q+1):
            if(s1[i-1]==s2[j-1]):
                mat[i][j]=1+mat[i-1][j-1]
            else:
                mat[i][j]=max(mat[i-1][j],mat[i][j-1])
    return mat[p][q]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()
    s2 = input()
    p = len(s1)
    q = len(s2)
    mat = [[0 for i in range(5001)]for j in range(5001)]
    result = commonChild(s1, s2, p, q, mat)

    fptr.write(str(result) + '\n')

    fptr.close()
