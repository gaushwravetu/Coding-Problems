# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:01:40 2020

@author: Gaurav
"""
#travelling salesman problem
def tsp(graph,s,n):
    vertex=[]
    for i in range(n):
        if i!=s:
            vertex.append(i)
for _ in range(int(input())):
    n = int(input())
    l1 = []
    s = 0
    v = 0
    for i in range(n):
        l = list(map(int,input().split()))
        l1.append(l)
    print(tsp(l1,s,n))