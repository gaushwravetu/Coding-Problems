for _ in range(int(input())):
    S=input()
    P=input()

    freqCount=[0]*26
    for s in S:
        freqCount[ord(s)-97]+=1
    for p in P:
        freqCount[ord(p)-97]-=1

    ans='';add=1
    pivot=ord(P[0])-97
    for i in range(1,len(P)):
        if P[i]>P[0]:
            break
        if P[i]<P[0]:
            add=0;break


    for i in range(pivot+add):
        while freqCount[i]!=0:
            ans+=chr(97+i)
            freqCount[i]-=1
    ans+=P

    for i in range(pivot+add,26):
        while freqCount[i]!=0:
            ans+=chr(97+i)
            freqCount[i]-=1

    print(ans)