for i in range(int(input())):
    n = int(input())
    mylist = list(map(int,input().split()))
    count = 0
    _2count = mylist.count(2)
    _0count = mylist.count(0)
    if _2count>1:
        count+=(_2count*(_2count-1))//2
    if _0count>1:
        count+=(_0count*(_0count-1))//2
    print(count)