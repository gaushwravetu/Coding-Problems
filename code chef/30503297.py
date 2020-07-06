for _ in range(int(input())):
    row,column = map(int,input().split())
    MyHardCodeList = [(2,2),(3,1),(4,2),(5,1),(6,2),(7,1),(8,2),(7,3),(6,4),(5,3),(4,4),(3,3),(2,4),(1,3),(2,4),(1,5),(2,6),(3,5),(4,6),(5,5),(6,6),(7,5),(8,4),(7,5),(8,6),(7,7),(8,8),(7,7),(6,8),(5,7),(4,8),(3,7),(2,8),(1,7)]
    mysize = len(MyHardCodeList)
    if(row==1 and column==1):
        print(mysize)
        for res in MyHardCodeList:
            print(*res)
    else:
        MyHardCodeList = [(4,4),(1,1)] + MyHardCodeList
        myindex = MyHardCodeList.index((row,column))
        mysize+=2
        print(mysize)
        for i in range(myindex,mysize):
            print(*MyHardCodeList[i])
        for i in range(myindex):
            print(*MyHardCodeList[i])
            