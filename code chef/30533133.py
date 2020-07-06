for _ in range(int(input())):
    NoOfPlayers = int(input())
    RatingList = list(map(int,input().split()))
    anslist = []
    for i in range(0,NoOfPlayers-2):
        anslist.append(RatingList[i]+RatingList[i+1]+RatingList[i+2])
    anslist.append(RatingList[0]+RatingList[-1]+RatingList[-2])
    anslist.append(RatingList[-1]+RatingList[0]+RatingList[1])
    #print(anslist)
    print(max(anslist))