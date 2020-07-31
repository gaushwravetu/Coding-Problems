for i in range(int(input())):
    people = int(input())
    peopleList = list(map(int,input().split()))
    flag = True
    _5count=0;_10count=0
    if(peopleList[0]==10 or peopleList[0]==15):
        print('NO')
    else:
        for i in range(people):
            if peopleList[i]==5:
                _5count+=1
                continue
            elif peopleList[i]==10 and _5count>0:
                _10count+=1
                _5count-=1
                #print(_5count,_10count)
                continue
            elif peopleList[i]==15 and (_5count>1 or _10count>0):
                if _10count>0:
                    _10count-=1
                else:
                    _5count-=2
            else:
                flag=False
                break
        if(flag):
            print('YES')
        else:
            print('NO')