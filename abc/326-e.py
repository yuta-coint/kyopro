N = int(input())
A = [0]+list(map(int,input().split()))
mod = 998244353
mat = pow(N,mod-2,mod)
dp = [1]
dp_sum = [1]
for i in range(N):
    dp.append(dp_sum[i]*mat%mod)
    dp_sum.append((dp_sum[i]+dp[i+1])%mod)
ans = 0
for i in range(1,N+1):
    ans+=dp[i]*A[i]%mod
    ans%=mod
print(ans)