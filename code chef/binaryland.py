def binmax(a,b):
    test1 = "{0:b}".format(bin(a))
    test2 = "{0:b}".format(bin(b))
    binXplusY = test1+test2
    binYplusX = test2+test1
    XplusY = int(binXplusY,2)
    YplusX = int(binYplusX,2)
    return XplusY-YplusX
for i in range(int(input())):
    N = int(input())
    mylist = list(map(int,input().split()))
    for i in range(N):
        for j in range(i+1,N):
            result = binmax(mylist[i],mylist[j])
            myresult = max(result,myresult)
    print(myresult)

