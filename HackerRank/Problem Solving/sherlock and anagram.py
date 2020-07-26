#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    mydict = Counter(s)
    count = 0
    for i in range(2,len(s)):
        mysubstr = s[0:i]
        lenmysubstr = len(mysubstr)
        mydict["".join(sorted(mysubstr))]+=1
        for j in range(1,len(s)):
            if j+lenmysubstr<=len(s):
                mydict["".join(sorted(s[j:j+lenmysubstr]))]+=1
    #print(mydict)
    for i in mydict:
        count+=mydict[i]*(mydict[i]-1)//2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
