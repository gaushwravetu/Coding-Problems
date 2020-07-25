# cook your dish here
for i in range(int(input())):
    N, K = map(int,input().split())
    mystr = ""
    mylist = list(map(int,input().split()))
    for i in mylist:
        if(i%K==0):
            mystr+='1'
        else:
            mystr+='0'
    print(mystr)