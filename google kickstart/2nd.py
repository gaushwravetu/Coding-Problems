import math
def square(result):
    result = math.sqrt(result)
    return((result - math.floor(result))==0)
for _ in range(int(input())):
    N = int(input())
    mylist = list(map(int,input().split()))
    count = 0
    for i in range(N):
        result = 0
        for j in range(i,N):
            result+=abs(mylist[j])
            if(square(result)):
                count+=1
    print("Case #{}: {}".format(_+1,count))
    
