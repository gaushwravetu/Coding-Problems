for t in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    flag = False
    N1=N2=sum_1=0
    for i in range(n):
        N1+=A[i]
        N2+=B[i]
    if(len(set(A))+len(set(B))==2):
        if(A[0]>B[0]):
            print(N2)
            flag = True
        else:
            print(N1)
            flag = True
    for i in range(n):
        if(A[i]<B[i]):
            sum_1+=A[i]
        else:
            sum_1+=B[i]
    if(not flag):
        print(sum_1)
        