    n,m = list(map(int,input().split()))
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    for i in range(len(l2)):
        l1.append(l2[i])
    l1.sort()
    for x in l1:
        print(x,end = " ")
    print()
        