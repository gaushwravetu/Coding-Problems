#!/bin/python3

import sys


S = input().strip()
try:
    myint = int(S)
    print(myint)
except ValueError:
    print('Bad String')
