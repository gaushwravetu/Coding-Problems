#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
resultString = ""
for i in range(m):
    for j in range(n):
        resultString+=matrix[j][i]
result = (re.compile(r'(\w)(\W+)(\w)')).sub(r"\1 \3",resultString)
print(result)
