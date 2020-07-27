def sum_digits(n):
    s = 0
    while n:
        s+=n%10
        n//=10
    return s
for i in range(int(input())):
    n = int(input())
    result = 0;chefCount=0;mortyCount=0
    for j in range(n):
        chef,morty = map(int,input().split())
        chefScore = sum_digits(chef)
        mortyScore = sum_digits(morty)
        if chefScore==mortyScore:
            chefCount+=1
            mortyCount+=1
        elif chefScore>mortyScore:
            chefCount+=1
        else:
            mortyCount+=1
    if(chefCount==mortyCount):
        print("{} {}".format(2, chefCount))
    elif(chefCount>mortyCount):
        print("{} {}".format(0, chefCount))
    else:
        print("{} {}".format(1, mortyCount))