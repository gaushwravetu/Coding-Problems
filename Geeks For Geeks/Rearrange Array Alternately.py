t = int(input())
for _ in range(t):
    n = int(input())
    l = list(input().split())
    for i in range(0, len(l)) : 
        l[i] = int(l[i]) 
    l.sort(reverse=True) 
    #print(l)
    l1 = []
    i = 0
    j = len(l)-1
    #print(i,j)
    while j>i:
        l1.append(l[i])
        l1.append(l[j])
        i+=1
        j-=1
    if(i==j):
        l1.append(l[i])
    #print(l1)
    for z in l1:
        print(z,end = " ")
    print()