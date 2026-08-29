N,M = map(int,input().split())
if N == 1 or N==2:
    print(1)
    exit()
mod  =10**9+7
fac = [1]
for i in range(1,2*(10**7)):
    fac.append(fac[-1]*i%mod)
fac_rev = [pow(fac[-1],-1,mod)]
for i in reversed(range(1,2*(10**7))):
    fac_rev.append(fac_rev[-1]*i%mod)
fac_rev.reverse()
out = fac[N]*pow((N-1)*(N-2)%mod,-1,mod)%mod
ans = 0
for m in range(N-2):
    if M<m:
        continue
    if m+N<M:
        continue
    ans += fac[N+m-1]*fac_rev[m+1]%mod*fac_rev[m]%mod*fac_rev[N-3-m]%mod*fac_rev[M-m]%mod*fac_rev[N-M+m]%mod
    ans %= mod
print(ans*out%mod)