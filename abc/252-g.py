mod = 998244353
N=int(input())
P=list(map(lambda x:int(x)-1,input().split()))
dp = [[0 for j in range(N+1)] for i in range(N)]
for i in range(N):
    dp[i][i+1]=1
for w in range(2,N):
    for j in range(1,N+1-w):
        dp[j][j+w]=dp[j+1][j+w]
        if P[j]<P[j+1]:
            dp[j][j+w]+=dp[j+1][j+w]
        for k in range(2,w):
            if P[j]<P[j+k]:
                dp[j][j+w]+=dp[j+1][j+k]*dp[j+k][j+w]%mod
                dp[j][j+w]%=mod
        #print(j,j+w,dp[j][j+w])
    #print("###############")
print(dp[1][N]%mod)

