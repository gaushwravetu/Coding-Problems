#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice, scores_count, alice_count):
    scores = sorted(list(set(scores)),reverse=True)
    alice.sort(reverse=True)
    result = []*alice_count
    j = 0
    scores_count = len(scores)
    for i in range(alice_count):
        while j<scores_count and alice[i]<scores[j]:
            j+=1
        result.append(j+1)
    result.sort(reverse=True)
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice, scores_count, alice_count)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
