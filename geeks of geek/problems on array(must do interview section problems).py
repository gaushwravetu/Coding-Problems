# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 13:29:07 2020

@author: Gaurav
"""

#Subarray with given sum
t = int(input())
for _ in range(t):
    n , s = list(map(int,input().split()))
    l = list(map(int,input().split()))
    mysum = 0
    i = 0
    found=False
    for j in range(len(l)):
        mysum+=l[j]
        while(mysum>s):
            mysum-=l[i]
            i+=1
        if(mysum==s):
            found = True
            print(i+1,j+1)
            break
    if (not found):
        print(-1)
        
#count the triplets
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    i = len(l)-1
    count = 0
    while i>=0:
        a = l[i]
        b = 0
        c = i-1
        while b<c:
            x = 0
            x =  l[b]+l[c]
            if(x==l[i]):
                count+=1
                b+=1
                #print(b,c)
            elif (x<a):
                b+=1
            else:
                c-=1
        i-=1
    if(count==0):
        print(-1)
    else:
        print(count)

#kedane's algorithm
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    sum = max(l)
    l1=[]
    l1.append(sum)
    for i in range(len(l)):
        sum = 0
        for j in range(i,len(l)):
            sum+=l[j]
            l1.append(sum)
    print(l1)
    print(max(l1))

#2nd approach
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    local_sum = l[0]
    global_sum = l[0]
    for j in range(1,len(l)):
        local_sum = max(l[i],local_sum+l[i])
        global_sum = max(local_sum,global_sum)
    print(global_sum)


#missing number in an array
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    mysum = int(n*(n+1)/2)
    series_sum = 0
    #print(mysum)
    for i in range(len(l)):
        series_sum+=l[i]
    result = int(mysum - series_sum)
    print(result)
    

#Merge Without Extra Space
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(input().split())
    for i in range(0, len(l)) : 
        l[i] = int(l[i]) 
    l.sort(reverse=True) 
    print(l)
    l1 = []
    i = 0
    j = len(l)-1
    print(i,j)
    while j>i:
        l1.append(l[i])
        l1.append(l[j])
        i+=1
        j-=1
    if(i==j):
        l1.append(l[i])
    print(l1)
    for z in l1:
        print(z,end = " ")
    print()
    
#Number of pairs
import math
t = int(input())
for _ in range(t):
    n, r = list(map(int,input().split()))
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    l1 = set(l1)
    l2 = set(l2)
    l1 = list(l1)
    l2 = list(l2)
    count = 0
    res1 = 0
    res2 = 0
    for j in range(len(l1)):
        for k in range(len(l2)):
            if(l1[j]==1 or l1[j]==2 or l1[j]==3 or l1[j]==4):
                if l1[j]!=l2[k]:
                    if l1[j]**l2[k]>l2[k]**l1[j]:
                        count+=1
            else:
                res1 = l1[j]*(math.log(l2[k]))
                res2 = l2[k]*(math.log(l1[j]))
                if(res2>res1):
                    count+=1
    print(count)
#Finding middle element in a linked list
class node:
    def __init__(self):
        self.data = None
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
t = int(input())
mylist = linkedlist()
for _ in range(t):
    n = int(input())
    for _ in range(n):
    data = int(input())
    node = node()
    node.data = data
    node.next = self.head
    self.head = None
#sort 0s 1s and 2s of list       
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    for z in l:
        print(z,end = " ")
    print()

#inversion of array
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    count = 0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if(l[i]>l[j]):
                count+=1
    print(count)
        



t = int(input())
for _ in range(t):
    n, a, b, c = list(map(int,input().split()))
    l = list(map(int,input().split()))
    l1 = []
    l2 = []
    for i in range(len(l)):
        l2.append(abs(l[i]-a))
        l1.append(abs(l[i]-b))
        
    p = min(l1) + min(l2)
    p = p + c
    print(p)
        
t = int(input())
for _ in range(t):
    n = int(input())
        l1 = []
        for  _  in range(n):
             s,p,v = list(map(int,input().split()))
             profit = int(int(p//(s+1))*v)
             l1.append(profit)
        print(max(l1))
             
#reverse the from the kth index
Python solution:

t = int(input())
while t>0:
nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]
arr = list(map(int, input().split()))
tmp = []
aux = []
j = 0
m = k
for i in range(int(n/k)):
aux = arr[j:m]
tmp += aux[::-1]
j = m
m += k
rem = n%k
if rem != 0:
aux = arr[n-rem:n]
tmp += aux[::-1]
print(*tmp)
t -= 1             
                 
            
        
for _  in range(int(input())):
    n,index = map(int,input().split())
    l = list(map(int,input().split()))
    j = 0
    l1 = []
    l2 = []
    for i in range(int(n/index)):
        l1 = l[j:index]
        l2+=l1[::-1]
    print(l1)
    print(l2)

#second approach
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    start = 0
    while start < N:
        print(*reversed(arr[start:start+K]),end=' ')
        start += K
    print()
    
            
for _  in range(int(input())):
    l = list(map(str,input().split(".")))
    l = '.'.join(l[::-1])
    print(l) 


# 0  1 knapsack problem
def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)]  
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
for _ in range(int(input())):
    n = int(input())
    W = int(input())
    val = list(map(int,input().split()))
    wt = list(map(int,input().split()))
    print(knapsack(W,wt,val,n))



#stock problem
#include<bits/stdc++.h>
#include<iostream>
using namespace std;
void get(int arr[],int n)
{
    int i=0,a=0,b=0;
    while(i<n-1)
    {
        while(i<n-1 && arr[i+1]<=arr[i])
        i++;
        if(i==n-1)
        break;
        a=i++;
        while(i<n && arr[i]>=arr[i-1])
        i++;
        b=i-1;
        cout<<"("<<a<<" "<<b<<")"<<" ";
    }
    if(a==0 && b==0)
    cout<<"No Profit";
}
int main()
{
    int t; cin>>t;
    while(t--)
    {
        int n; cin>>n; int arr[n];
        for(int i=0;i<n;i++)cin>>arr[i];
        get(arr,n);
        cout<<"\n";
    }
    return 0;
}       
        
        
if '1' in arr:
one_pos = arr[::-1].index('1')
print(len(arr)-one_pos-1)
else:
print("-1")
test-=1        
        
        
        
        
        
        
        
        
        