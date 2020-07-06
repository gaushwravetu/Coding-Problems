# cook your dish here
# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    master=[]
    for i in range(k):
        master.append([])
    for i in range(n):
        master[i%k].append(A[i])
    for i in range(k):
        master[i].sort()
    subA=[]
    for i in range(n):
        subA.append(master[i%k].pop(0))
    flag=True
    for i in range(1,n):
        if subA[i-1]>subA[i]:
            flag=False
            break
    print('yes' if flag else 'no')