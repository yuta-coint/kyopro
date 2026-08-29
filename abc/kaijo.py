#階乗とその逆元の列挙######################
mod = 998244353
fac = [0 for i in range(3*(10**7))]
fac[0] = 1
for i in range(1, 3*(10**7)):
    fac[i] = i * fac[i - 1] %mod
fac_rev = [0] * (3*(10**7))
fac_rev[-1] = pow(fac[-1], -1, mod)
for i in reversed(range(1, 3*(10**7))):
    fac_rev[i - 1] = fac_rev[i] * i %mod
############################################