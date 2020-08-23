for _ in range(int(input())):
    N = int(input())
    k = 2
    result = 0
    while(True):
        if(N%((2**k)-1)==0):
            break
        k+=1
    result = N//((2**k)-1)
    print(result)