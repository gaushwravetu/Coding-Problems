def k(x,y):
    if(int(str(x)+str(y))<(int(str(y)+str(x)))):
        return 1
    else:
        return -1
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(str,input().split()))
    l = sorted(l,key=functools.cmp_to_key(k))
    print("".join(l))