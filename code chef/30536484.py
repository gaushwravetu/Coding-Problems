# cook your dish here
from collections import defaultdict
for _ in range(int(input())):
    NoOfTurns = int(input())
    P,Q = map(int,input().split())
    file1 = list(map(int,input().split()))
    file2 = list(map(int,input().split()))
    file3 = list(map(int,input().split()))
    binaryList = list(input())
    fileDict3 = defaultdict(int)
    (sumkillF,sumassistF,sumkillD,sumassistD,resultF,resultD,result) = (0,0,0,0,0,0,0)
    for i in file3:
        fileDict3[i]+=1
    #print(fileDict3)
    for i in range(NoOfTurns):
        result = file1[i] + file2[i]
        if(fileDict3[result]>0 and binaryList[i] == '0'):
            fileDict3[result]-=1
            sumkillF+=file1[i]
            sumassistF+=file2[i]
        if(fileDict3[result]>0 and binaryList[i] == '1'):
            fileDict3[result]-=1
            sumkillD+=file1[i]
            sumassistD+=file2[i]    
    resultF = P*sumkillF + Q*sumassistF
    resultD = P*sumkillD + Q*sumassistD
    #print(resultF,resultD)
    if(resultF>resultD):
        print('Frost')
    else:
        print('DustinKiller')
            