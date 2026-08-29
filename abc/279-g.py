N,K,C = map(int,input().split())
mod = 998244353
if C == 1:
    print(1)
    exit()
elif C==2:
    print(pow(2,N,mod))
    exit()
dp = [0 for i in range(N+1)]
half  = pow(2,mod-2,mod)
pow2k = pow(2,K,mod)
dp[0]=1
for i in range(1,K+1):
    dp[i]=(C*(C-1)%mod*half%mod*(pow(2,i,mod)-2)%mod+C)%mod
#後ろk-1個が全部同じ色のやつを数える
dp2 = [0 for i in range(N+1)]
for i in range(K-1):
    dp2[i]=C
dp2[K-1] = C
dp2[K] = C*C%mod
for i in range(K+1,N+1):
    #2色から選ぶ
    dp[i]=(dp[i-1]*2%mod+dp2[i-1]*(C-2)%mod)%mod
    #前K-1個が全部同じ色なら色変えができる
    dp2[i]=(dp[i-(K-1)]*2%mod+dp2[i-(K-1)]*(C-2)%mod)%mod
#print(dp)
#print(dp2)
print(dp[N])

