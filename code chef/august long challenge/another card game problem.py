for i in range(int(input())):
    chef, rick = map(int,input().split())
    cc=0;rc=0;rrem=0;crem=0
    cc+=chef//9
    crem = chef%9
    if crem>0:
        cc+=1
    rc+=rick//9
    rrem = rick%9
    if rrem>0:
        rc+=1
    if cc>=rc:
        print(1,rc)
    else:
        print(0,cc)