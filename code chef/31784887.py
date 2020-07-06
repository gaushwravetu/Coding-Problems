import sys  
sys.setrecursionlimit(10**9) 
MOD=10**9+7
from collections import defaultdict


def dfs(visited,tree,path,u,v):
    if not visited[u]:
        visited[u]=True
        path.append(u)
        if(u==v):
            return True
        found=False
        for x in tree[u]:
            found=dfs(visited,tree,path,x,v)
            if found:
                return True
        path.pop()
    return False


def findpath(tree,u,v,N):
    path=[]
    visited=[False]*(N+1)
    dfs(visited,tree,path,u,v)
    return path

   
def primefactors(N):
    pf=defaultdict(int)
    count=0
    while(N%2==0):
        count+=1;N/=2;
    if count>0:
        pf[2]=count
    x=3
    while(N>1):
        count=0;
        while(N%x==0):
            count+=1;N/=x;
        if count>0:
            pf[x]=count
        x+=2
    return pf
    
    
for _ in range(int(input())):
    NoOfNodes = int(input())
    tree=defaultdict(list)
    for _ in range(NoOfNodes-1):
        u,v = map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)
    CostOfNodes = list(map(int,input().split()))
    NoOfQuery = int(input())
    querylist = []
    for _ in range(NoOfQuery):
        U,V = map(int,input().split())
        querylist.append((U,V))
    
    ans=[]
    factorsList=[]
    
    for i in range(NoOfNodes):
        factorsList.append(primefactors(CostOfNodes[i]))
    for i in range(len(querylist)):
        path=findpath(tree,querylist[i][0],querylist[i][1],NoOfNodes)
        div=defaultdict(int)
        for p in path:
            for y in factorsList[p-1]:
                div[y]+=factorsList[p-1][y]
        d=1
        for x in div:
            d=(d*(div[x]+1))%MOD
        ans.append(d%MOD)
    print(*ans,sep='\n')
            
    