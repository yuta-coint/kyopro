mod = 998244353
fac = [0 for i in range(10**7)]
fac[0] = 1
for i in range(1, 10**7):
    fac[i] = i * fac[i - 1] %mod
fac_rev = [0] * (10**7)
fac_rev[-1] = pow(fac[-1], -1, mod)
for i in reversed(range(1, 10**7)):
    fac_rev[i - 1] = fac_rev[i] * i %mod
#後で書く。
import sys
sys.setrecursionlimit(10**7)
# a_k の値を x に更新
def update(k, x):
    k += N0-1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = min(data[2*k+1], data[2*k+2])
# 区間[l, r)の最小値
def query(l, r):
    L = l + N0; R = r + N0
    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R-1])

        if L & 1:
            s = min(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s
def calc(l,r):
    m = query(l,r) % (10**6)
    if r - l <= 1:
        return 1
    base = calc(l, m) * calc(m + 1, r) % mod
    t1 = m - l
    t2 = r - (m + 1)
    if l == 0 and r == N:
        return base * fac[t1 + t2] % mod * fac_rev[t1] % mod * fac_rev[t2] % mod
    elif l == 0:
        #print(l,r,base * fac[t1 + t2 + 1] % mod * fac_rev[t1] % mod * fac_rev[t2 + 1] % mod)
        return base * fac[t1 + t2 + 1] % mod * fac_rev[t1] % mod * fac_rev[t2 + 1] % mod
    elif r == N:
        return base * fac[t1 + t2 + 1] % mod * fac_rev[t1 + 1] % mod * fac_rev[t2] % mod
    else:
        c = fac[t1 + t2 + 1] % mod * fac_rev[t1] % mod * fac_rev[t2 + 1] % mod
        c += fac[t1 + t2 + 1] % mod * fac_rev[t1 + 1] % mod * fac_rev[t2] % mod
        c %= mod
        c -= fac[t1 + t2] % mod * fac_rev[t1] % mod * fac_rev[t2] % mod
        c %= mod
        return base * c % mod

N = int(input())
N0 = 2**(N-1).bit_length()
INF = 2**31-1
data = [INF]*(2*N0)

# 前計算
I = []; J = []
for x in range(N0, 2*N0+1):
    y = (x // (x & -x)) >> 1
    I.append((y << 1)-1 if y else 0)
    J.append(y << 1)
J.reverse()
N0 = 2**(N-1).bit_length()
INF = 2**63-1
data = [INF]*(2*N0)

P = list(map(int,input().split()))
for i in range(N):
    update(i,- P[i] * (10**6) + i)
print(calc(0,N))
