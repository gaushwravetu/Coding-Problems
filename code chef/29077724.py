#exam cheating
import math   
t = int(input())
for _ in range(t):
    n, r = list(map(int,input().split()))
    l1 = []
    if n == r:
        print(-1)
    else:
        if(n>r):
            p = n-r
            t = int(p**0.5)
            for i in range(1,t+1):
                if(p%i==0):
                    l1.append(i)
                    l1.append(p//i)
            #print(l1)
            l1 = set(l1)
            print(len(l1))
            
        else:
            p = r-n
            t = int(p**0.5)
            for i in range(1,t+1):
                if(p%i==0):
                    l1.append(i)
                    l1.append(p//i)
            l1 = set(l1)
            print(len(l1))
            #print(l1)