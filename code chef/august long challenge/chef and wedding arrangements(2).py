from collections import defaultdict

for _ in range(int(input())):
    N, K= map(int, input().split())
    F = list(map(int, input().split()))

    dp=[[0 for i in range(N)] for j in range(N)]
    dp[0][0]=K

    dd = defaultdict(int)
    dd[F[0]]=1

    for i in range(1,N):
        if dd[F[i]]==1:
            dp[i][0]=dp[i-1][0] + 2
        elif dd[F[i]]>1:
            dp[i][0]=dp[i-1][0] + 1
        else:
            dp[i][0]=dp[i-1][0]
        dd[F[i]]+=1



    for j in range(1,N):
        if dp[j-1][j-1] + K <= dp[j][j-1]:
            dp[j][j]= dp[j-1][j-1] + K
            dd=defaultdict(bool)
            dd[F[j]]=1
            for i in range(j+1,N):
                if dd[F[i]]==1:
                    dp[i][j]=dp[i-1][j] + 2
                elif dd[F[i]]>1:
                    dp[i][j]=dp[i-1][j] + 1
                else:
                    dp[i][j]=dp[i-1][j]
                dd[F[i]]+=1
        else:
            dp[j][j]=dp[j][j-1]
            for i in range(j,N):
                dp[i][j]=dp[i][j-1]
        # print(dp,dd)

    print(dp[N-1][N-1])