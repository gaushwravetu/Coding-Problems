import math
def divisor(M):
    l1 = []
    for i in range (1,int(math.sqrt(M))+1):
        if(M%i==0):
            if M/i==i:
                l1.append(i)
            else:
                l1.append(i)
                l1.append(M//i)
    return l1
for _ in range(int(input())):
    A,M = map(int,input().split())
    my_array = []
    l1 = divisor(M)
    l1.remove(M)
    #print(l1)
    for i in (l1):
        if((M-i)%A==0 and ((M-i)//A)%i==0):
            my_array.append((M-i)//A)
    my_array.sort()
    #print(my_array)
    print(len(my_array))
    print(*(my_array))