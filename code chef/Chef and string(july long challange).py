for i in range(int(input())):
    N = int(input())
    mylist = list(map(int,input().split()))
    result = 0
    for i in range(N-1):
        if mylist[i]==mylist[i+1]:
            continue
        else:
            result+= abs(mylist[i]-mylist[i+1])-1
    print(result)