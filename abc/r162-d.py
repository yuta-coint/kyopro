mod = 998244353
#i=1からN-1までに対し、iを一番左にするような部分集合で、補集合の平均値が1で大きさがjのものが何個あるかを数えればよい。
fac = [0 for i in range(10**7)]
fac[0] = 1
for i in range(1, 10**7):
    fac[i] = i * fac[i - 1] % mod

fac_rev = [0] * (10**7)
fac_rev[-1] = pow(fac[-1], -1, mod)
for i in reversed(range(1, 10**7)):
    fac_rev[i - 1] = fac_rev[i] * i % mod
N = int(input())
dp = [0 for i in range(N + 1)]
dp[0] = 1
d = list(map(int, input().split()))
const = 0
for i in range(N - 2):
    const += fac[i] * fac[N - 3 - i] % mod * fac_rev[N - 3] % mod
    const %= mod
print(const)
ans = 0
for i in reversed(range(N)):
    if i == 0 or d[i] == 0:
        ans += N - 2
        ans %= mod
    elif N - i - d[i] >= 0:
        ans += dp[N - i - d[i]] * d[i] % mod * const % mod
        ans %= mod
    for j in reversed(range(N + 1)):
        if j == 0 and d[i] == 0:
            continue
        elif j == 0 and d[i] != 0:
            dp[j] = 0
            continue
        elif j >= d[i]:
            dp[j] = dp[j - 1] + dp[j - d[i]]
        else:
            dp[j] = dp[j - 1]
        dp[j] %= mod
    print(ans)
    print(dp)
ans *= fac[N - 3]
for i in range(N):
    if i == 0:
        ans *= fac_rev[d[0] - 1]
        ans %= mod
    else:
        ans *= fac_rev[d[i]]
        ans %= mod
print(ans)