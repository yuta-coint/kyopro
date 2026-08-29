mod = 998244353
N,K = map(int,input().split())
fac = [1]
for i in range(1,10**6):
    fac.append(fac[-1]*i%mod)
fac_inv = [pow(fac[-1],mod-2,mod)]
for i in reversed(range(1,10**6)):
    fac_inv.append(fac_inv[-1]*i%mod)
fac_inv.reverse()
pt = [0 for t in range(N)]
for t in range(N):
    ruiseki = 0
    for i in range(N):
        if i<=K:
            if N-i-1<t:
                continue
            pt[t]+=fac[N-i-1]%mod*fac[N-1-t]%mod*i%mod*fac_inv[N-i-1-t]%mod
            pt[t]%=mod
        elif i<=2*K:
            if N-i-1>=t:
                ruiseki += fac[N-i]*fac[N-1-t]%mod*fac_inv[N-i-t]%mod
                pt[t]+=fac[N-i-1]*fac[N-1-t]%mod*fac_inv[N-i-1-t]%mod*(2*K-i)%mod
                pt[t]%=mod
            pt[t]+=ruiseki
            pt[t]%=mod
            if i==2*K:
                record= ruiseki
                if N-i-1>=t:
                    record+=fac[N-i-1]*fac[N-1-t]%mod*fac_inv[N-i-1-t]%mod*K%mod
                    record%=mod
        else:
            pt[t]+=record
            pt[t]%=mod
        #print(ruiseki,pt[t])
#print(pt)
A = list(map(int,input().split()))
A.sort()
ans = 0
for i in range(N):
    ans += A[i]*pt[i]%mod
    ans %= mod
ans *= 2
ans %= mod
print(ans)