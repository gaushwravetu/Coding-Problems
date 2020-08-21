for i in range(int(input())):
    darth,chef = map(int,input().split())
    i = chef
    while(i>0):
        if darth<=0:
            break
        darth-=i
        i=i//2
        print(darth,i)
    if(darth>0):
        print('0')
    else:
        print('1')
