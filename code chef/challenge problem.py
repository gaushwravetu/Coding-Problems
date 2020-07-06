# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:40:27 2020

@author: Gaurav
"""

for _ in range(int(input())):
    n = int(input())
    l1 = []
    for _ in range(n):
        p = int(input())
        l1.append(p)
    #print(l1)
    mymax = max(l1)
    print(mymax)





#2nd problem
for _ in range(int(input())):
    n = int(input())
    count = 0
    #mysum = 0
    l1 = list(map(int,input().split()))
    for i in range(n):
        if(l1[i]%2==0):
            count+=1
    print(count*(n-count))
       




def solve(visited,power,n,m, i,j,p,count):
    if power[i][j]>=p:
        return count
    if i==n:
        return count
    if j==m:
        return count
     if not visited[i][j]:
        visited[i][j]=True
    else:
        return count
    count+=solve(visited,power,n,m,i+1,j,p,count)
    count+=solve(visited,power,n,m,i-1,j,p,count)
    count+=solve(visited,power,n,m,i,j+1,p,count)
    count+=solve(visited,power,n,m,i,j-1,p,count)
    return count

for _ in range(int(input())):
    n,m,r = map(int,input().split())
    power=[]
    for i in range(n):
        l=list(map(int,input().split()))
        power.append(l)
    query=[]
    for i in range(r):
        a,b,c=map(int,input().split())
        query.append((a,b,c))
    for x in power:
        print(x)
    for x in query:
        print(x)
    answer=[]
    for i in range(r):
        visited=[]
        for k in range(n):
            l=[False]*m
            visited.append(l)
        a=solve(visited,power,n,m, query[i][0]-1,query[i][1]-1,query[i][2],0)
        answer.append(a)
    for x in answer:
        print(x)
        
        
        
#COG2003     
for _ in range(int(input())):
   NoOfPlayers = int(input())
   RatingList = list(map(int,input().split()))
   anslist = []
   for i in range(0,N)
           #print(anslist)
   print(max(anslist))
        
        
for _ in range(int(input())):
    A,B = map(int,input())
    a = []
    b = []
    result = []
    a.append(A//10)
    a.append(A%10)
    b.append(B//10)
    b.append(B%10)
    (r1,r2,r3,r4) = [0,0,0,0]
    r1 = a[0]*10+b[0]
    r2 = b[0]*10+a[0]
    r2 = a[1]*10+b[1]
    r3 = b[1]*10+a[1]        
    result.append(r1+r3)
    result.append(r2+r4)
    result.append(A+B)
    print(max(result))    
        
        
#hackwithinfy
for _ in range(int(input())):
    n = int(input())
    mylist = list(map(float,input().split()))
    mylist.sort()
    (leftindex,trip) = (0,0)
    for i in range(n-1,-1,-1):
        if(mylist[i]>1.99):
            trip+=1
        elif(mylist[i]<=1.99):
            if(mylist[i]+mylist[leftindex]<=3.00):
                leftindex+=1
            trip+=1
        if(leftindex>=i):
            break
    print(trip)


#understanding the sequence
for i in range(int(input())):
    n = int(input())
    result = "1"
    while(n>1):
        current = ""
        i = 0
        while(i<len(result)):
            count = 1
            while(i+1<len(result) and result[i]==result[i+1]):
                count+=1
                i+=1
            current+=str(count)+result[i]
            i+=1
        result = current
        n-=1
    print(current)
            

#game of pile-       
for i in range(int(input())):
    mylist = list(map(int,input().split()))




import keyword
keyword.kwlist
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        