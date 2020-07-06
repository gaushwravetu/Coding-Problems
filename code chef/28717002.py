#dynamo
t = int(input())
for _ in range(t):
    n = int(input())
    A = int(input())
    P = int(10 ** n)
    if(A>0 and A<P):
        S = int(2*P + A)
        print(S,flush = True)
    else:
        break
    B = int(input())
    if(B>0 and B<P and (A+B)<S):
        C = (P - B)
        print(C,flush = True)
    else:
        break
    D = int(input())
    if(D>0 and D<P and (A+B+C+D)<S):
        E = (P - D)
        print(E,flush = True)
    else:
        break
    i = input()