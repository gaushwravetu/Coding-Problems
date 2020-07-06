 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(charlist):
    length = len(charlist)
    w =  [char for char in charlist]
    first = length-1
    (swapelement,second_swap_element) = (0,0)
    while(first>=1):
        if(w[first]>w[first-1]):
            swapelement = first-1
            second_swap_element = first
            break
        first-=1
    if(second_swap_element==0):
        return("no answer")
    else:
        for i in range(second_swap_element+1,length):
            if(w[swapelement]<w[i] and w[i]<w[second_swap_element]):
                second_swap_element = i
    #print(swapelement,second_swap_element)
    (w[swapelement],w[second_swap_element])=(w[second_swap_element],w[swapelement])
    #print(swapelement,second_swap_element)
    #print(w)
    w[swapelement+1:] = sorted(w[swapelement+1:])
    return ("".join(w))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
