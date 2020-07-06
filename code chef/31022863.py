# cook your dish here
for _ in range(int(input())):
    NoOfCars = int(input())
    listOfCars = list(map(int,input().split()))
    listOfCars.sort(reverse=True)
    TotalNoOfCars = len(listOfCars)
    result = listOfCars[0]
    p = 1000000007
    for i in range(1,TotalNoOfCars):
        if(listOfCars[i]-i<=0):
            break
        else:
            result+=listOfCars[i]-i
    print(result%p)