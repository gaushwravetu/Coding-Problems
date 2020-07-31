for i in range(int(input())):
    items,k = map(int,input().split())
    pricelist = list(map(int,input().split()))
    Total = sum(pricelist)
    newTotal = 0
    for i in pricelist:
        if i>k:
            newTotal+=k
        else:
            newTotal+=i
    print(Total-newTotal)