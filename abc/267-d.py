N,M = map(int,input().split())
A = list(map(int,input().split()))
dp = [-float("inf") for j in range(M+1)]
dp[0]=0
for i in range(N):
    for j in reversed(range(1,M+1)):
        dp[j] = max(dp[j],dp[j-1]+A[i]*j)
print(dp[M])
