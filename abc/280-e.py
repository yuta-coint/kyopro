N,P = map(int,input().split())
mod = 998244353
dp = [0 for i in range(N+1)]
cri = P*pow(100,mod-2,mod)%mod
fan = (100-P)*pow(100,mod-2,mod)%mod
dp[0]=0
dp[1]=1
for i in range(2,N+1):
    dp[i]=(dp[i-1]+1)*fan%mod+(dp[i-2]+1)*cri%mod
    dp[i]%=mod
print(dp[N])