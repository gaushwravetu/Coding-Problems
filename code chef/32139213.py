# cook your dish here
for _ in range(int(input())):
    S = str(input())
    R = str(input())
    N = len(S)
    Gaplist = []
    (GapLength,Length,NoOfSwap) = (0,0,0)
    flag = False
    for i in range(N):
        if(S[i]==R[i]):
            if(flag):
                GapLength+=1
        else:
            if(not flag):
                NoOfSwap+=1
            flag = True
            Length+=1
            if(GapLength>0):
                NoOfSwap+=1
                Gaplist.append(GapLength)
                GapLength = 0
    Gaplist.sort()
    MinPossibleOutcome = NoOfSwap*Length
    for i in range(len(Gaplist)):
        NoOfSwap-=1
        Length+=Gaplist[i]
        MinPossibleOutcome = min(MinPossibleOutcome,NoOfSwap*Length)
    print(MinPossibleOutcome)
        