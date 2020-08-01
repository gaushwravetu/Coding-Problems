def check(cc,ini,fin,a,b,c):
    dif0 = fin[0]-ini[0]
    dif1 = fin[1]-ini[1]
    dif2 = fin[2]-ini[2]
    #print(dif0,dif1,dif2,a,b,c,cc)
    if cc==3:
        return 0
    elif cc==2:
        return 1
    elif(a==1):
        if dif1==dif2 and fin[1]>ini[1] and fin[2]>ini[i]:
            return 1
        elif ini[1]!=0 and ini[2]!=0 and ini[1]%fin[1]==0 and fin[2]%ini[2]==0 and fin[1]//ini[1]==fin[2]//ini[2]:
            return 1
        else:
            return 2
    elif(b==1):
        if dif0==dif2 and fin[0]>ini[0] and fin[2]>ini[2]:
            return 1
        elif ini[0]!=0 and ini[2]!=0 and fin[0]%ini[0]==0 and fin[2]%ini[2]==0 and fin[0]//ini[0]==fin[2]//ini[2]:
            return 1
        else:
            return 2
    elif(c==1):
        if dif0==dif1 and fin[0]>ini[0] and fin[1]>ini[1]:
            return 1
        elif ini[1]!=0 and ini[1]!=0 and fin[0]%ini[0]==0 and fin[1]%ini[1]==0 and fin[0]//ini[0]==fin[1]//ini[1]:
            return 1
        else:
            return 2
    else:
        if dif0==dif1==dif2 and dif0>0 and dif1>0 and dif2>0:
            return 1
        elif ini[0]!=0 and ini[1]!=0 and ini[2]!=0 and fin[0]%ini[0]==0 and fin[2]%ini[2]==0 and fin[1]%ini[1]==0 and fin[0]//ini[0]==fin[1]//ini[1]==fin[2]//ini[2]:
            return 1
        elif dif0==dif1 and dif0>0 and dif1>0:
            return 2
        elif ini[0]!=0 and ini[1]!=0 and fin[0]%ini[0]==0 and fin[1]%ini[1]==0 and fin[0]//ini[0]==fin[1]//ini[1]:
            return 2
        elif dif1==dif2 and dif1>0 and dif2>0:
            return 2
        elif ini[1]!=0 and ini[1]!=0 and fin[1]%ini[1]==0 and fin[1]%ini[1]==0 and fin[1]//ini[1]==fin[1]//ini[1]:
            return 2
        elif dif0==dif2 and dif0>0 and dif2>0:
            return 2
        elif ini[0]!=0 and ini[2]!=0 and fin[0]%ini[0]==0 and fin[2]%ini[2]==0 and fin[0]//ini[0]==fin[2]//ini[2]:
            return 2
        elif dif2<0 or dif1<0 and dif0<0:
            return 0
        else:
            return 3
        
        

for i in range(int(input())):
    intial = list(map(int,input().split()))
    final = list(map(int,input().split()))
    (a,b,c,count) = (0,0,0,0)
    if intial[0]==final[0]:
        a+=1
        count+=1
    if intial[1]==final[1]:
        b+=1
        count+=1
    if intial[2]==final[2]:
        c+=1
        count+=1
    result = check(count,intial,final,a,b,c)
    print(result)

