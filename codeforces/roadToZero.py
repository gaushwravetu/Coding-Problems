for _ in range(int(input())):
    LEN1,LEN2=map(int,input().split())
    ALEN,BLEN=map(int,input().split())
    if BLEN<=2*ALEN:
        LEN1,LEN2=min(LEN1,LEN2),max(LEN1,LEN2)
        ANSWER=LEN1*BLEN+(LEN2-LEN1)*ALEN
    else:
        ANSWER=(LEN2+LEN1)*ALEN
    print(ANSWER)