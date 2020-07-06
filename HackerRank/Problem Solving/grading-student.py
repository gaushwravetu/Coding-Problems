#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    gradelist = []
    for i in range(len(grades)):
        prev_result = grades[i]
        new_grade = grades[i]%5
        if(new_grade>2):
            grades[i]+=5-new_grade
            if(grades[i]>=40):
                gradelist.append(grades[i])
            else:
                gradelist.append(prev_result)
        else:
            gradelist.append(prev_result)
    return gradelist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
