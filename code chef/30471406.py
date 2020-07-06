from collections import defaultdict
MyTestCase,MySubCase = map(int,input().split())
for _ in range(MyTestCase):
    NoOfTurns = int(input())
    AttakerList = list(map(int,input().split()))
    DefenderList = list(map(int,input().split()))
    OnTablelist = defaultdict(int)
    AttakerList.sort()
    DefenderList.sort()
    AttakerList.append(-9999)
    DefenderList.append(-9999)
    flag = True
    count = 0
    i = 0
    while AttakerList[i] > -9999:
        ka = AttakerList[i]
        if(ka<DefenderList[i] and flag==True):
            kd = DefenderList[i]
            OnTablelist[ka]
            OnTablelist[kd]
            count+=1
            flag = False
        elif(ka<DefenderList[i] and ka in OnTablelist):
            kd = DefenderList[i]
            OnTablelist[ka]
            OnTablelist[kd]
            count+=1
        i+=1
    if(count == NoOfTurns):
        print('YES')
    else:
        print('NO')
