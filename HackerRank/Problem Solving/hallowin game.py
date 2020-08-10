#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    count=1
    s-=p
    if s<=0:
        return 0
    else:
        while(s>0):
            if p>m:
                p-=d
                # print(p)
                if s>0 and p>=m and s-p>0:
                    s-=p
                    count+=1
                if s==0:
                    return count
            elif p<=m:
                    count+=s//m
                    # print(s)
                    # print(m)
                    return count
                    # s-=m
                    # count+=1
                    # if s==0:
                    #     return count
                    # else:
                    #     while(s>0):
                    #         if s==0:
                    #             return count
                    #         s-=m
                    #         count+=1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
