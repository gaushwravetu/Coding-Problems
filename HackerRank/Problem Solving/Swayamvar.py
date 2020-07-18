n = int(input())
brideStr = input()
groomStr = input()
groomR = 0
groomM = 0
for i in groomStr:
    if(i=='r'):
        groomR+=1
    else:
        groomM+=1
Total = 0
for j in brideStr:
    if(j=='r'):
        if(groomR>0):
            groomR-=1
            Total+=1
        else:
            break
    else:
        if(groomM>0):
            groomM-=1
            Total+=1
        else:
            break
print(n-Total)

    