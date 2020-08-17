from collections import defaultdict
N,W,D = map(int,input().split())
nlist = list(map(int,input().split()))
A=0;B=0
Alist = []
Blist = []
mydict = {}
for i in range(N-W+1):
    mysum = (sum(nlist[i:i+W]))
    mysum = max(mysum,(sum(nlist[i:i+W])))
    mydict[i+1]=((sum(nlist[i:i+W])))
for i in range(len(mydict)):



