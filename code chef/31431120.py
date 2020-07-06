for i in range(int(input())):
    NoOfSequence = int(input())
    ListSequence = list(map(int,input().split()))
    _2list = []
    GeneratedSequence = 0
    for i in range(NoOfSequence):
        if(ListSequence[i]%2==0):
            ListSequence[i] = ListSequence[i]/2
            if(ListSequence[i]%2==0):
                _2list.append(2)
            else:
                _2list.append(1)
        else:
            _2list.append(0)
    i=0
    while i<NoOfSequence:
        j=i;zCount=0;
        while j<NoOfSequence and _2list[j]==0:
            zCount+=1
            j+=1
        GeneratedSequence+=((zCount+1)*zCount)//2
        if j!=NoOfSequence:
            if _2list[j]==2:
                GeneratedSequence+=(zCount+1)*(NoOfSequence-j)
                j+=1
            elif _2list[j]==1:
                k=j+1
                while k<NoOfSequence:
                    if _2list[k]!=0:
                        break
                    k+=1
                if k!=NoOfSequence:
                    GeneratedSequence+=(zCount+1)*(NoOfSequence-k)
                j+=1
        i=j
    print(GeneratedSequence)