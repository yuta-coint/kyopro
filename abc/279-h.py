N, M = map(int,input().split())
mod = 200003
fac = [1]
for i in range(1,mod):
    fac.append(fac[-1]*i%mod)
invfac = [0]*mod
invfac[-1] = pow(fac[-1],-1,mod)
for i in range(mod-2,-1,-1):
    invfac[i] = invfac[i+1]*(i+1)%mod
def comb_with_Lucas(n, k):
    if k < 0 or k > n:
        return 0
    res = 1
    while n > 0 or k > 0:
        n_mod = n % mod
        k_mod = k % mod
        if k_mod > n_mod:
            return 0
        res = res * fac[n_mod] % mod
        res = res * invfac[k_mod] % mod
        res = res * invfac[n_mod - k_mod] % mod
        n //= mod
        k //= mod
    return res
ans = comb_with_Lucas(M + N - 1, 2 * N - 1)
k = 1
while k*(3 * k  - 1) <= 2 * (M - N):
    sgn = -1 if k % 2 else 1
    t1 = k*(3 * k - 1)//2
    if t1 >= 0:
        ans = (ans + sgn * comb_with_Lucas(M + N - t1 - 1, 2 * N - 1)) % mod
    t2 = k*(3 * k + 1)//2
    if t2 >= 0:
        ans = (ans + sgn * comb_with_Lucas(M + N - t2 - 1, 2 * N - 1)) % mod
    #print(M,N,t1,t2,ans,M + N - t1 - 1, 2 * N - 1,M + N - t2 - 1, 2 * N - 1)
    k += 1
print(ans % mod)