# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:25:20 2020

@author: Gaurav
"""

#exam cheating
import math   
t = int(input())
for _ in range(t):
    n, r = list(map(int,input().split()))
    l1 = []
    if n == r:
        print(-1)
    else:
        if(n>r):
            p = n-r
            #t = int(p**0.5)
            for i in range(1,t+1):
                if(p%i==0):
                    l1.append(i)
                    l1.append(p//i)
            l1 = set(l1)
            print(len(l1))
            print(l1)
            
        else:
            p = r-n
            #t = int(p**0.5)
            for i in range(1,t+1):
                if(p%i==0):
                    l1.append(i)
                    l1.append(p//i)
            l1 = set(l1)
            print(len(l1))
            print(l1)
        
        
        
#chef_chick
t = int(input())
for _ in range(t):
    p = int(input())
    l1 = list(map(int,input().split()))
    l1.sort()
    print(l1[0])


#RGAND problem         
t = int(input())
for _ in range(t):
    n, r = list(map(int,input().split()))
    while n<=r:
        b = bin(n).replace("0b","")
        print(b)
        n+=1
       
      
       
t = int(input())
for _ in range(t):
    l, r = [int(v) for v in input().split()]
    b = bin(l)[2:]
    p = 1
    s = 0
    res = 0
    for i in range(len(b)-1, -1, -1):
        if b[i] == '1':
            res += p * min(p-s, r-l+1)
            res %= 1000000007
            s += p
        p *= 2
    print(res)

       
       
#cookoff feb
def max_sum(l,n):
    max = 0
    msis = [0 for x in range(n)]
    for i in range(n):
        msis[i]=l[i]
    for i in range(1,n):
        for j in range(i):
            if(l[i]>l[j] and msis[i]<msis[j]+l[i]):
                msis[i] = msis[i]}+l[i]
        
        
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    n = max_sum(l,n)
    
          
       



#tax problem
def tax1(n):
    tax = 0
    tincome = n
    if(n<250000):
        tincome-=tax
    elif(n>250000 and n<=500000):
        tax+=(n-25000)*(0.05)
        tincome-=tax
    elif(n>500000 and n<=750000):
        tax+=12500+(n-500000)*(0.10)
        tincome-=tax
    elif(n>750000 and n<=1000000):
        n-=12500+25000+(n-750000)*(0.15)
        tincome-=tax
    elif(n>1000000 and n<=1250000):
        tax+=12500+25000+37500+(n-1000000)*(0.20)
        tincome-=tax
    elif(n>1250000 and n<=1500000):
        tax+=12500+25000+37500+50000+(n-1250000)*(0.25)
        tincome-=tax
    else(n>1500000):
        tax+=12500+25000+37500+50000+62500+(n-1500000)*(0.30)
        tincome-=tax
    return tincome
for _ in range(int(input())):
    n = int(input())
    result = tax1(n)
    print(int(result))
    
#goal shots
for _ in range(int(input())):
    n = int(input())
    A,B = (0,0)
    l = list(map(int,input().split()))
    for i in range(0,len(l),2):
        A+=l[i]
        B+=l[i+1]
    print(A,B)
    
    






       
       
       
       
       
       