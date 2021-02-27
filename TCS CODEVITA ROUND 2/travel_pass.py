def myfun(a,b,c):
    if(a>=c):
        return 0
    if(dp[a]!=-1):
        return dp[a]
    while(b[a]!=1):
        a+=1
        if(a>=c):
            return 0
    mycost = 10**9
    for i in range(5):
        ttemp = mylist2[i]+myfun(req_cost+mylist1,array,7*n)
        mycost = min(mycost,temp)
    dp[a]=mycost
    return mycost
N = 280002
dp = [0]*N    
mylist1 = list(map(int,input().split()))
mylist2 = list(map(int,input().split()))
n = int(input())
array = [0]*(7*n+2)
for i in range(n):
    mystr = input()
    for j in range(7):
        dp[i*7+j]=-1
        if mystr[j]=="X":
            array[i*7+j]=1
        else:
            array[i*7+j]=0

price = 10**9
req_cost = 0
while(array[req_cost]!=1):
    if(req_cost==7*n):
        break
    req_cost+=1
if(req_cost==7*n):
    print(0)
else:
    for i in range(5):
        temp = mylist2[i]+myfun(req_cost+mylist1,array,7*n)
        mycost = min(mycost,temp)
    print(mycost)

