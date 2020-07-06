from collections import defaultdict as dd
def getset(n,list1):
    i=0
    for s in list1:
        if i == n:
            return s
        i+=1
    
T=int(input())
for _ in range(T):
    N,K=map(int,input().split())
    P=list(map(int,input().split()))
    ans=[];case1=0
    for i in range(N):
        if P[i]!=N-i:
            case1=1
            break
    
    checker=set(); cycle=set()
    for i in range(N):
        if P[i]!=i+1:
            checker.add(i)
    impossible=False;dlen=len(checker); k=0
    while True:
        if dlen==0:
            break
        else:
            x=getset(0,checker)
            y=P[x]-1
            z=P[y]-1
            if z==x:
                cycle.add(x); checker.remove(x); dlen-=1;
                cycle.add(y); checker.remove(y); dlen-=1;
            else:
                if k<K:
                    ans.append("{} {} {}".format(x+1,y+1,z+1))
                    k+=1; 
                else:
                    impossible=True; break
                temp=P[z]; P[z]=P[y]; P[y]=P[x]; P[x]=temp;
                if P[y]==y+1: 
                    checker.remove(y)
                    dlen-=1
                if P[x]==x+1: 
                    checker.remove(x)
                    dlen-=1
                if P[z]==z+1: 
                    checker.remove(z)
                    dlen-=1


    if len(cycle)==0 and len(checker)==0:
        impossible=False
    elif len(cycle)==0 and len(checker)==2:
        impossible=True
    else:
        dlen=len(cycle)
        if dlen%4==0:
            while dlen>0:
                a=getset(0,cycle); cycle.remove(a); dlen-=1;
                b=P[a]-1; cycle.remove(b); dlen-=1;
                c=getset(0,cycle); cycle.remove(c); dlen-=1;
                d=P[c]-1; cycle.remove(d); dlen-=1;
                if k<K:
                    ans.append("{} {} {}".format(a+1,b+1,c+1))
                    k+=1; 
                else:
                    impossible=True; break
                if k<K:
                    ans.append("{} {} {}".format(a+1,d+1,c+1))
                    k+=1; 
                else:
                    impossible=True; break


        else:
            impossible=True
    if impossible:
        print(-1)
    else:
        num=len(ans)
        print(num)
        if num>0:
            print(*ans,sep="\n")