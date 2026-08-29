mod = 998244353
N,M = map(int,input().split())
#両端が同じ
dp = [1,M]
#両端が異なる
dp_sub = [0,0]
for i in range(2,N+2):
    dp.append(dp_sub[i-1])
    dp_sub.append(((M-1)*dp[i-1]%mod+(M-2)*dp_sub[i-1]%mod)%mod)
print(dp[-1])