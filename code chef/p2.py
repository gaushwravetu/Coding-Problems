def prime(num):
    if num > 1:
   # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
        else:
            print(num,"is a prime number")
for _ in range(int(input())):
    n=int(input())
    mylist=list(map(int, input().split()))
    mylist.sort(reverse=True)
    
    if n==1:
        print("first")
        continue
    if n==2:
        if mylist[0]>mylist[1]:
            print("first")
        elif mylist[0]==mylist[1]:
            print("draw")
        else:
            print("second")
        continue
    
    
    i=3; first=mylist[0];second=mylist[1]+mylist[2]
    
    if n>3:
        while i<n:
            if i%2==1:
                first+=mylist[i]
            else:
                second+=mylist[i]
            i+=1
    
    if first>second:
        print("first")
    elif first==second:
        print("draw")
    else:
        print("second")