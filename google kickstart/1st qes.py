for _ in range(int(input())):
    N,T = map(int,input().split())
    mylist = list(map(int,input().split()))
    i = 0;mount=0;
    while(i<N-1):
        K = T
        #print(mylist[i],mylist[i+1])
        if mylist[i]==K and mylist[i]-mylist[i+1]==1:
            K-=2
            if(K==0):
                mount+=1
                i+=2
            else:
                j = i+1
                while(j<N-1):
                    #print(mylist[j],mylist[j+1])
                    if(mylist[j]-mylist[j+1]!=1):
                        break
                    else:
                        K-=1
                        if(K==0):
                            mount+=1
                            break
                    j+=1
                i=j+1
        else:
            i+=1
    print('Case #{}: {}'.format(_+1,mount))
