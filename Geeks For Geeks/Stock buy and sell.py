def max_profit(arr,n):
    (k,i,flag)=(0,0,0)
    n=len(arr)
    arr.append(-99)
    l=[]
    while(arr[i]!=-99):
        if arr[i]<arr[i+1] and flag==0:
            start=i
            l.append(start)
            flag=1
        elif arr[i]>arr[i+1] and flag==1:
            end = i
            l.append(end)
            flag = 0
        i+=1
    
    if(len(l)==0):
        print("No Profit")
    else:
        for i in range(0,len(l)-1,2):
            print("({} {})".format(l[i],l[i+1]),end = " ")
        print()
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    #for i in range(n-1):
    max_profit(arr,n)
    