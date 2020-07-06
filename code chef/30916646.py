# cook your dish here
for _ in range(int(input())):
    mylist = list(map(int,input().split()))
    mylist.sort()
    if(mylist[0]*mylist[2] == mylist[1]*mylist[3]):
        print('YES')
    else:
        print('NO')