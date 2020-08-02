from itertools import product
N,K = map(int,input().split())
ANS=0;MYSUM=0
my = list()
for i in range(N):
    mylist = list(map(int,input().split()))[1:]
    my.append(mylist)
r = map(lambda x:sum(i*i for i in x)%K,product(*my))
print(max(r))
