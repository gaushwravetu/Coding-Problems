for _ in range(int(input())):
    NoOfInput,sets=map(int,input().split())
    list1=list(map(int,input().split()))
    list2=list(map(int,input().split()))
    (supp,poss)=(101,101)
    i = 0
    while(i<NoOfInput):
        if list2[i]==0:
            supp=min(supp,list1[i])
        else:
            poss=min(poss,list1[i])
        i+=1
    if supp+poss<=100-sets:
        print('yes')
    else:
        print('no')