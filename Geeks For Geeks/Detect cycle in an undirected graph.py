def isCyclicUtil(g,v,visited,parent):
    visited[v]=True
    #count = 0
    #print(v,end=' ')
    for i in g[v]:
        if not visited[i]:
            if(isCyclicUtil(g,i,visited,v)==1):
                return(1)
        elif parent!=i:
            return(1)
    return(0)
def isCyclic(g,N):
    # code here
    visited = [False for i in range(N)]
    for i in range(N):
        if not visited[i]:
            if(isCyclicUtil(g,i,visited,-1)==1):
                return(1)
    return(0)


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict

#Contributed by : Nagendra Jha

#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N,E = map(int,input().strip().split())
        g = Graph(N)
        edges = list(map(int,input().strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)
        print(isCyclic(g.graph,N))
# } Driver Code Ends