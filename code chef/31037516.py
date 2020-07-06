# cook your dish here
for _ in range(int(input())):
    NoOfSpots = int(input())
    footList = list(map(int,input().split()))
    footListlen = len(footList)
    flag = True
    count = 0
    for i in range(footListlen):
        if(footList[i]==1 and count==0):
            count+=1
            j = i
        elif(footList[i]==1 and count==1):
            if(i-j>=6):
                j=i
            else:
                flag = False
                break
        if(not flag):
            break
    if(flag):
        print('YES')
    else:
        print('NO')
            