T=int(input())
for _ in range(T):
    N=int(input())
    if ((N//2)%2)!=0:
        print("NO")
    else:
        evenlist=[];x=2
        for i in range(N//2):
            evenlist.append(x)
            x=x+2
        evensum=sum(evenlist)
        oddlist=[];x=1
        for i in range((N//2)-1):
            oddlist.append(x)
            x=x+2
        last=evensum-sum(oddlist)
        oddlist.append(last)
        print("YES")
        print(*evenlist, sep=" ",end=" ")
        print(*oddlist,sep=" ")