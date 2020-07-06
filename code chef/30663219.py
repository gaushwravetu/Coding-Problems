for _ in range(int(input())):
    noOfMoves = int(input())
    mylist = list(map(int,input().split()))
    toosweet = max(mylist)
    mylist2 = []
    z = int(noOfMoves/2)
    (j,count,mount) = (0,0,0)
    for i in range(noOfMoves):
        if(mylist[i]<toosweet):
            j+=1
            
        else:
            mylist2.append(j)
            j = 0
    mylist2.append(j)
    if mylist2[-1]==toosweet:
        mylist2.append(0)
    myresult=mylist2[0]+mylist2[-1]
    mylist2[0] = myresult
    mylistlen = len(mylist2)
    for i in range(mylistlen-1):
        if mylist2[i]>=z:
            count+=mylist2[i]-z+1
    print(int(count))
            
            
            
            