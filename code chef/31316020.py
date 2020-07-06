# cook your dish here
for _ in range(int(input())):
    NoOfDivisors,NoOfPrimes = map(int,input().split())
    count = 0
    while(NoOfDivisors%2==0):
        NoOfDivisors = NoOfDivisors/2
        count+=1
    x = 3
    while(x*x<NoOfDivisors):
        while(NoOfDivisors%x==0):
            NoOfDivisors = NoOfDivisors/x
            count+=1
        x+=2
    if(NoOfDivisors>2):
        count+=1
    if(count>=NoOfPrimes):
        print(1)
    else:
        print(0)
    