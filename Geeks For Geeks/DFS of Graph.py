def mydfs(g,v,visited):
    visited[v]=True
    print(v,end=' ')
    for i in g[v]:
        if not visited[i]:
            visited[i]=True
            mydfs(g,i,visited)
def dfs(g,N):
    '''
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the dfs of the graph from node 0, newline is given by driver code
    '''
    # code here
    visited = [False for i in range(N)]
    mydfs(g,0,visited)
    #v=0
   
    #print(type(l))
    

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

        dfs(g.graph,N) # print bfs of graph
        print()

# } Driver Code Ends