for i in range(int(input())):
    mynum = int(input())
    result = 0
    count = 0
    for i in range(1,mynum+1):
        result+=i
        count+=1
        if(result>mynum):
               print(count-1)
               break
        elif(result==mynum):
               print(count)
               break
                    
