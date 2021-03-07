from collections import defaultdict
def prefixString(a,b):
    mystrdict = defaultdict(int)
    n = len(a)
    prefix = ""
    for i in range(n):
        for j in range(i,n):
            prefix = a[i]+a[j]
            mystrdict[prefix]+=1
    for j in b:
        if mystrdict[j]==1:
            return True
    return False
a = ['one','twothree','four']
b = ['onetwo','one']
print(prefixString(a,b))