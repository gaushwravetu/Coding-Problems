for _ in range(int(input())):
    noOfMoves = int(input())
    steps = list(input())
    (x,y)=(0,0)
    (count,mount,sount,rount) = (0,0,0,0)
    for i in range(noOfMoves):
        if(steps[i]=='L' and count==0 and sount==0):
            x-=1
            count = 1
            mount = 0
            sount = 1
            rount = 0
        elif(steps[i]=='R'and sount==0 and count==0 ):
            x+=1
            count = 0
            mount = 0
            sount = 1
            rount = 0
        elif(steps[i]=='U' and mount==0 and rount==0):
            y+=1
            mount = 1
            count = 0
            sount = 0
            rount = 1
        elif(steps[i]=='D' and rount==0 and mount==0):
            y-=1
            mount = 1
            count = 0
            sount = 0
            rount = 1
            
    print(x,y)
