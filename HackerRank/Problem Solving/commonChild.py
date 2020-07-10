import math
import os
import random
import re
import sys
maximum = 5001
# Complete the commonChild function below.
def commonChild(s1, s2, p, q, mat):
    if(p==0 or q==0):
        return 0
    if(mat[p-1][q-1]!=-1):
        return mat[p-1][q-1]
    if(s1[p-1]==s2[q-1]):
        mat[p-1][q-1] = 1+commonChild(s1,s2,p-1,q-1, mat)
        return mat[p-1][q-1]
    else:
        mat[p-1][q-1] = max(commonChild(s1,s2,p,q-1,mat),commonChild(s1,s2,p-1,q,mat))
        return mat[p-1][q-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()
    p = len(s1)
    q = len(s2)

    mat = [[-1 for i in range(maximum)] for i in range(maximum)]
    result = commonChild(s1, s2, p, q, mat)

    fptr.write(str(result) + '\n')

    fptr.close()