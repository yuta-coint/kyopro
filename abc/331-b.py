N,S,M,L = map(int,input().split())
dp = [10**9 for i in range(N+1)]
dp[0]=0
for i in range(1,N+1):
    if i<6:
        if dp[i]>S:
            dp[i]=S
    else:
        if dp[i]>dp[i-6]+S:
            dp[i] = dp[i-6]+S
    if i<8:
        if dp[i]>M:
            dp[i]=M
    else:
        if dp[i]>dp[i-8]+M:
            dp[i] = dp[i-8]+M
    if i<12:
        if dp[i]>L:
            dp[i]=L
    else:
        if dp[i]>dp[i-12]+L:
            dp[i] = dp[i-12]+L
print(dp[-1])