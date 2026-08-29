N = int(input())
a = list(map(int,input().split()))
dp = [0 for i in range(N)]
dp[0]=a[0]
dp[1]=a[0]
for i in range(2,N):
    dp[i]=min(dp[i-1]+a[i],dp[i-2]+a[i-1])
ans = dp[N-1]
dp = [0 for i in range(N)]
dp[0]=0
dp[1]=min(a[0],a[1])
for i in range(2,N):
    dp[i]=min(dp[i-1]+a[i],dp[i-2]+a[i-1])
ans = min(ans,dp[N-2]+a[N-1])
print(ans)