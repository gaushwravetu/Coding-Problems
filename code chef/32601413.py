for i in range(int(input())):
    X,Y,left,right = map(int,input().split())
    m=len(bin(min(X,Y))[2:])
    if(X*Y==0):
        print(0)
        continue
    res=bin(X|Y)[2:]
    rb=len(bin(right)[2:])-1
    res=res[::-1]
    s=res[:rb]
    s=s[::-1]
    if len(s)==0:
        print(1)
        continue
    print(int(s,2))