#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def check(mystr):
    str_len = len(mystr)
    for i in range(str_len//2):
        if mystr[i]!=mystr[str_len-1-i]:
            return 1
    return 0
def palindromeIndex(s):
    str_len = len(s)
    for i in range(str_len//2):
        if s[i]!=s[str_len-1-i]:
            if(i+1<str_len):
                myfun = check(s[i+1:str_len-i])
                if myfun==1:
                    return str_len-i-1
                return i
    return -1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
