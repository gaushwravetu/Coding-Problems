T=int(input())
for _ in range(T):
    N=input()
    N=int(N)
    a=list(map(int,input().split()))
    ans=0
    if a[0]<0:
        flag=False
    else:
        flag=True
    x=0;prev=a[0]
    while x<N:
        if flag:
            if a[x]>0:
                prev=max(prev,a[x])
            else:
                ans=ans+prev
                prev=a[x]
                flag=False
        else:
            if a[x]<0:
                prev=max(prev,a[x])
            else:
                ans=ans+prev
                prev=a[x]
                flag=True
        x+=1
    print(ans+prev)