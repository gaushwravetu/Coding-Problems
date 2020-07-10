import collections
def bfs(graph,N):
    '''
    can use queue module already imported
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the bfs of the graph from node 0, newline is given by driver code
    '''
    # code here
    visited, queue = set(), collections.deque([0])
    visited.add(0)
    while queue: 
        vertex = queue.popleft()
        print(vertex,end=" ")
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict
import queue
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
            g.addEdge(u,v) # add a directed edge from u to v

        bfs(g.graph,N) # print bfs of graph
        print()

# } Driver Code Ends