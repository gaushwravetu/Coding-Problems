for i in range(int(input())):
    players,chef = map(int,input().split())
    playerlist = list(map(int,input().split()))
    result = 0
    minresult = 10**9
    ans = 0
    flag = False
    for i in range(players):
        if chef%playerlist[i]==0:
            flag=True
            result = chef//playerlist[i]
            minresult = min(result,minresult)
            if(result<=minresult):
                ans = playerlist[i]
    if(not flag):
        print('-1')
    else:
        print(ans)


