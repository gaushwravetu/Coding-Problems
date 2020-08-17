from itertools import product
l = []
for i in range(int(input())):
    n = int(input())
    mylist = list(map(int,input().split()))
    l.append(mylist)
print(list(product(*l)))
