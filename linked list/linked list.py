# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 18:04:18 2020

@author: Gaurav
"""
#source geeks for geeks
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,"")
            temp = temp.next
    def insertafter(self,prev_data,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        prev = self.head
        while(prev.next!=prev_data):
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node
    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
if __name__=='__main__':
    prev_data, new_data = list(map(int,input().split()))
    llist = linkedlist()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next=second
    second.next=third
    #third.next=None;
    llist.insertafter(prev_data,new_data)
    llist.append(new_data)
    llist.printList()
    
#deletion in linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node
    def deleteNode(self,data):
        temp = self.head
        if(temp is not None):
            if(temp.data==data):
                temp = None
        while(temp is not None):
            if(temp.data==data):
                break
            #print(temp.data)
            prev = temp
            temp = temp.next
        if(temp==None):
            return
        prev.next = temp.next
        temp=None
        
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
        
#Driver Program
llist = linkedlist()
llist.push(7)
llist.push(5)
llist.push(6)
llist.push(9)
llist.push(11)
llist.printlist()
llist.deleteNode(6)
llist.printlist() 




#GRAGHS
def mydef(self,v,visited):
        visited[v]=True
        print(v,end=' ')
        for i in self.graph(v):
            if visited == False:
                self.mydef(i,visited)
def dfs(self,v,n):
        #mark all the vertices as not visited
        visited = [False]*n
        self.mydfs(v,visited)
from collections import defaultdict
#this class represents a directed graph using adjacency list representation
class Graph:
    def __init__ (self,vertices):
        #default dictionary to store graph
        self.graph = defaultdict(list)
        self.v = vertices
    def addEdge(self,u,v):
        self.graph[u].append(v) #add directed edge from u to v
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n,e=map(int,input().strip().split())
        g = Graph(n)
        edges = list(map(int,input().strip().split()))
        for i in range(0,len(edges),2):
            u,v = edges[i]+edges[i+1]
            g.addEdge(u,v)
            g.addEdge(v,u)
        dfs(g.graph,n)
        print()
            
            
            
def isCyclicUtil(g,v,visited,parent):
    visited[v]=True
    count = 0
    #print(v,end=' ')
    for i in g[v]:
        if not visited[i]:
            count+=isCyclicUtil(g,i,visited,v)
        elif parent!=i:
            count+=1
    return count
def dfs(g,N):
    # code here
    visited = [False for i in range(N)]
    for i in range(N):
        if not visited[i]:
            count=(isCyclicUtil(g,i,visited,-1))
    if(count!=0):
        print(count)
    else:
        print(0)
    #v=0
   
    #print(type(l))

#finding the largest the number
import functools
def k(x,y):
    if(int(str(x)+str(y))<(int(str(y)+str(x)))):
        return 1
    else:
        return -1
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(str,input().split()))
    l = sorted(l,key=functools.cmp_to_key(k))
    print("".join(l))
    
        
    
#equilibrium point
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    result = 0
    lsum = 0
    flag = False
    for i in range(n):
        result+=l[i]
    for i in range(n):
        result-=l[i]
        if lsum==result:
            flag = True
            print(i+1)
            break
        lsum+=l[i]
    if(not flag):
        print(-1)
    
#tapping water problem
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    result = 0
    if(l[0]<=l[n-1]):
        for i in range(n-1):
            result+=l[0]-l[i]
    else:
        for i in range(1,n-1):
            result+=l[n-1]-l[n]




for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    lmax=a[0]
    rmax=max(a[1:])
    count=0
    for i in range(n):
        if(a[i]>lmax):
            lmax=a[i]
        if(a[i]==rmax and i<n-1):
            rmax=max(a[i+1:])
        h=min(lmax,rmax)
        count+=max(h-a[i],0)
    print(count)    

l = [3,4,1,2,5]
dict = {}
for x in l:
    dict[x*x]=1
print(dict)



l.sort(reverse=True)
    print(l1)
    print(l)
    for j in range(index-1):
        l.append(l1[i])
    print(l)





          