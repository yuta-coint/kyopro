N,D = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
y = [abs(q[i]-p[i]) for i in range(N)]
mod = 998244353
dp = [[0 for j in range(D+1)] for i in range(D+1)]
dp_sum = [[0 for j in range(D+1)] for i in range(D+1)]
dp_dif = [[0 for j in range(D+1)] for i in range(D+1)]
dp[0][0] = 1
for x in y:
    for i in range(D+1):
        for j in reversed(range(D+1)):
            if i==0 or j==D:
                dp_sum[i][j] = dp[i][j]
            else:
                dp_sum[i][j] = (dp_sum[i-1][j+1]+dp[i][j])%mod
    for i in range(D+1):
        for j in range(D+1):
            if j==0 or i==0:
                dp_dif[i][j] = dp[i][j]
            else:
                dp_dif[i][j] = (dp_dif[i-1][j-1]+dp[i][j])%mod
    for i in reversed(range(D+1)):
        for j in reversed(range(D+1)):
            if i+j<x:
                dp[i][j] = 0
            elif i<=x and j<=x:
                dp[i][j] = dp_sum[i+j-x][0]
            elif i>x and j<=x:
                dp[i][j] = (dp_sum[i+j-x][0]-dp_sum[i-x][j]+dp_dif[i-x][j])%mod
            elif i<=x and j>x:
                dp[i][j] = (dp_sum[i][j-x]+dp_dif[i][j-x]-dp[i][j-x])%mod
            else:
                dp[i][j] = (dp_sum[i][j-x]-dp_sum[i-x][j]+dp_dif[i-x][j]+dp_dif[i][j-x]-dp[i][j-x])%mod
        #print(dp[i])
ans = 0
for i in range(D+1):
    ans += sum(dp[i])%mod
    ans %= mod
print(ans)