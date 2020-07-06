for _ in range(int(input())):
    noOfPeople = int(input())
    infectedList = []
    listOfPeople = list(map(int,input().split()))
    for i in range(noOfPeople):
        k=1
        for j in range(i,0,-1):
            if listOfPeople[j]- listOfPeople[j-1]>2:
                break
            k+=1
        for j in range(i+1,noOfPeople):
            if listOfPeople[j]- listOfPeople[j-1]>2:
                break
            k+=1
        infectedList.append(k)
    print(min(infectedList),max(infectedList))