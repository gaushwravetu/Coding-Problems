def MyCalculatedFunction(xmas, ymas): 
    if(ymas == 0): 
        return 1
    MyVariable = MyCalculatedFunction(xmas, int(ymas / 2))  
    if (ymas % 2 == 0): 
        return (MyVariable * MyVariable)%(10**9+7) 
    else: 
        if(ymas > 0): 
            return ((xmas * MyVariable)%(10**9+7)* MyVariable)%(10**9+7) 
        else: 
            return (((MyVariable * MyVariable)%(10**9+7)) / xmas)%(10**9+7)
for _ in range(int(input())):
    NoInput,Astrix=map(int,input().split())
    MySummation=Astrix
    MyPrevious=MyCalculatedFunction(Astrix,2)
    i = 2
    while(i<NoInput+1):
        MyCurrent=(MyCalculatedFunction(MyPrevious,2*i-1))%(10**9+7)
        MySummation+=MyCurrent
        MySummation=MySummation%(10**9+7)
        MyPrevious=(MyCurrent*MyPrevious)%(10**9+7)
        i+=1
    print(MySummation%(10**9+7))