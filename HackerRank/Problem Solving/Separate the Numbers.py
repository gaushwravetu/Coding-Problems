#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    strlen = len(s)
    valid = False
    for i in range(strlen//2):
        substr = ""
        substr+=s[:i+1]
        #print(substr)
        validsubstr = substr
        num = int(s[:i+1])
        while(len(validsubstr)<strlen):
            num+=1
            validsubstr+=str(num)
            #print(validsubstr)
        if(validsubstr==s):
            valid = True
            break
    if(valid):
        print("{} {}".format('YES',substr))
    else:
        print('NO')

                 
    
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
