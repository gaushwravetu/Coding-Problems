from collections import defaultdict
class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addedge(self, u, v):
        self.graph[u].append(v)
        print(self.graph)
    def dfsTraverse(self,U,visited):
        visited[U]=True
        print(U)
        for i in self.graph[U]:
            if visited[i]==False:
                self.dfsTraverse(i,visited)
    def dfs(self):
        V = len(self.graph)
        visited = [False]*V
        for i in range(V):
            if visited[i]==False:
                self.dfsTraverse(i,visited)


g = graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)
print("ANS : ")
g.dfs()