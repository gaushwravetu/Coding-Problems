from collections import defaultdict
class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addedge(self, u, v):
        self.graph[u].append(v)
        print(self.graph)
    def bfs(self,s):
        visited = [False]*(len(self.graph))
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
g = graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(1,2)
g.addedge(2,0)
g.addedge(2,3)
g.addedge(3,3)
print("ANS : ")
g.bfs(2)

