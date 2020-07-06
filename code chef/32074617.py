for _ in range(int(input())):
    NoOfInput,Query=map(int,input().split())
    lengthofvictor,sumofvictor,i=(0,0,0)
    while(i<Query):
        anti,beta=map(int,input().split())
        sumofvictor+=abs(anti-lengthofvictor)
        lengthofvictor=beta
        sumofvictor+=abs(anti-beta)
        i+=1
    print(sumofvictor)