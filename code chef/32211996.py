# cook your dish here
for _ in range(int(input())):
    N,K = map(int,input().split())
    mylist = list(map(str,input().split()))
    (tCOUNT,hCOUNT) = (0,0)
    for i in range(N-K):
        if(mylist[i]=='T'):
            tCOUNT+=1
        else:
            hCOUNT+=1
    if(mylist[N-K]=='H'):
        print(tCOUNT)
    else:
        print(hCOUNT)