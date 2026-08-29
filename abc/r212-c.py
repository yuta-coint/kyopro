N, M = map(int,input().split())
mod = 998244353
if N < M:
    print(0)
    exit()
#階乗とその逆元の列挙######################
fac = [0 for i in range(3*(10**7))]
fac[0] = 1
for i in range(1, 3*(10**7)):
    fac[i] = i * fac[i - 1] %mod
fac_rev = [0] * (3*(10**7))
fac_rev[-1] = pow(fac[-1], -1, mod)
for i in reversed(range(1, 3*(10**7))):
    fac_rev[i - 1] = fac_rev[i] * i %mod
############################################
ans = 0
for i in range(N - M + 1):
    j = N - M - i
    temp = fac[i+3*M-1] * fac[j + M - 1]%mod*fac_rev[i] * fac_rev[3*M-1]%mod*fac_rev[j] % mod * fac_rev[M-1] % mod
    if j & 1:
        temp = -temp
    ans += temp
    ans %= mod
print(ans*pow(2, M, mod) % mod)
