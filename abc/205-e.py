N,M,K = map(int,input().split())
fact = [1]
mod = 10**9+7
for i in range(1,3*(10**6)):
    fact.append(fact[-1]*i%mod)
rev = [pow(fact[-1],mod-2,mod)]
for i in reversed(range(1,3*(10**6))):
    rev.append(rev[-1]*i%mod)
rev.reverse()
if N==K:
    print(fact[M+N]*rev[M]%mod*rev[N]%mod)
    exit()
if N>M+K:
    print(0)
    exit()
ans = 0
for i in range(N+1):
    ans += fact[2*N-K-1-i]*rev[N-i]%mod*rev[N-K-1]%mod*fact[M-N+K+i]%mod*rev[M-N+K]%mod*rev[i]%mod
    ans%=mod
for i in range(N-K):
    ans -= fact[2*N-K-1-i]*rev[N-K-1-i]%mod*rev[N]%mod*fact[M-N+K+i]%mod*rev[M-N+K]%mod*rev[i]%mod
    ans%=mod
print(ans)
