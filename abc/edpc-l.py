N = int(input())
#ここから何点取れるか[i,j)が残っている状態で
dp = [[0 for j in range(N+1)] for i in range(N+1)]
a = list(map(int,input().split()))
for ran in range(1,N+1):
    for l in range(N+1-ran):
        r = l+ran
        dp[l][r] = max(a[l]-dp[l+1][r],a[r-1]-dp[l][r-1])
print(dp[0][N])
