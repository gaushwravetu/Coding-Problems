for i in range(int(input())):
    N, M, X, Y = map(int,input().split())
    result = N*M
    ans = 0
    if(result==1):
        ans = X
    elif(X*2<=Y):
        ans = result*X
    elif(Y>=X):
        if(result%2==0):
            ans = (result//2)*Y
        else:
            ans = ((result//2))*Y + X
    else:
        ans = ((result+1)//2)*Y
    print(ans)