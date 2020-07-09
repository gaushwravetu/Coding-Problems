#import math
def pyth(n,l):
    dict = {}
    for x in l:
        dict[x*x]=1
    for i in range(n-1):
        for j in range(i+1,n):
            if(l[i]*l[i]+l[j]*l[j]) in dict:
                return 'Yes'
    return 'No'        
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    print(pyth(n,l))
       
        
    