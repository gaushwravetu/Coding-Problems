for _ in range(int(input())):
    NoOfPages = int(input())
    if(NoOfPages==1):
        print(1)
        print(1,1)
    else:
        GeneratedList = []
        if(NoOfPages%2==0):
            GeneratedList.append((1,2))
        else:
            GeneratedList.append((1,2,NoOfPages))
            NoOfPages = NoOfPages-1
        for i in range(3,NoOfPages,2):
            GeneratedList.append((i,i+1))
        print(len(GeneratedList))
        for i in GeneratedList:
            print(len(i),*i)