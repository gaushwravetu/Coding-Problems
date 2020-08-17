from itertools import repeat
from itertools import permutations
from collections import defaultdict
low,high = map(int,input().split())
k = int(input())
mylist = []
count = 0
mydict = {}
mod = 10**9+7
for i in range(low,high+1):
    mylist.extend(repeat(i,k))
perm = permutations(mylist,k)
for i in perm:
    mydict[i]=1
for i in mydict:
    res = 0
    res = sum(list(i))
    if res%2==0:
        count+=1
print(count%mod)