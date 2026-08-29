N = int(input())
A = list(map(int,input().split()))
dp = [[10**24 for i in range(N+1)] for j in range(N+1)]
xor = [[0 for i in range(N+1)] for j in range(N+1)]
for k in range(1,N+1):
    for i in range(N+1-k):
        j = i+k
        if k==1:
            xor[i][j]=A[i]
            dp[i][j]=A[i]
            continue
        xor[i][j] = A[i]^xor[i+1][j]
        if k&1:
            for l in range(1,k):
                if l&1:
                    temp=dp[i][i+l]+dp[i+l][j]+xor[i][j]-xor[i][i+l]
                else:
                    temp=dp[i][i+l]+dp[i+l][j]+xor[i][j]-xor[i+l][j]
                if dp[i][j]>temp:
                    dp[i][j]=temp
        else:
            for l in range(1,k):
                if l&1:
                    temp=dp[i][i+l]+dp[i+l][j]+xor[i][j]*2-xor[i][i+l]-xor[i+l][j]
                else:
                    temp=dp[i][i+l]+dp[i+l][j]
                if dp[i][j]>temp:
                    dp[i][j]=temp
print(dp[0][N])