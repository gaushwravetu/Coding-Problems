    lenString1,lenString2 = map(int,input().split())
    string1 = list(input())
    string2 = list(input())
    ResultantList =[]
    for i in range(lenString2+1):
        ResultantList.append([0]*(lenString1+1))
    result = 0
    for i in range(1,lenString2+1):
        for j in range(1,lenString1+1):
            if(string2[i-1]==string1[j-1]):
                #print(string2[i-1],string1[j-1])
                ResultantList[i][j] = ResultantList[i-1][j-1]+1
                result = max(ResultantList[i][j],result)
            else:
                ResultantList[i][j]=0
    #print(ResultantList)
    print(result)