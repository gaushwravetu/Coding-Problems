
from sys import *
import collections
import math

t = int(stdin.readline())
for _ in range(t):
    h,n = list(map(int,stdin.readline().split(' ')))
    ans = [0]*(n)
    l = []
    for i in range(n):
        t,x,a = list(map(int,stdin.readline().split(' ')))
        l.append((x,a,t,i))
    l.sort()
    for i in range(n):
        up = math.inf
        down = -math.inf
        xi = l[i][0]
        ai = l[i][1] 
        pi = l[i][3]
        for j in range(i+1,n,1):
            xj = l[j][0]
            pj = l[j][3]
            if(xj == xi):
                ans[pi] += 1
                ans[pj] += 1
                continue
            aj = l[j][1]
            t = l[j][2]
            s = (aj-ai)/(xj-xi)
            if(s > down and s < up):
                ans[pi] += 1
                ans[pj] += 1
            if(t == 1):
                up = min(up,s)
            else:
                down = max(down,s)
            if(up <= down):
                break
    for h in ans:
        print(h,end = ' ')
    print(' ')