#Equality
n , q = list(map(int,input().split()))
l1 = list(map(int,input().split()))
l2 = []    
for i in range(n-1):
    if(l1[i]<l1[i+1]):
        l2.append('i')
    else:
        l2.append('d') 
    #l2.sort()
    #print(l2)
for _ in range(q):
    l , r = list(map(int,input().split()))
    if(l2[l-1]==l2[r-2]):
        print("NO")
    else:
        print("YES")
