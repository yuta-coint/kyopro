from math import isqrt
N,M = map(int,input().split())
mod = 10**9+7
mother = pow(N-1, -1, mod)
L = isqrt(M)
# M//iになりうる数を列挙する。
M_over_i = []
for i in range(1, L):
    M_over_i.append(M // i)
for i in range((M//L) + 1):
    M_over_i.append(i)
M_over_i = sorted(M_over_i)
rd = {v: i for i, v in enumerate(M_over_i)}
#dp[rd[x]]:xを超えるまでの回数の期待値
dp = [0, N * mother % mod]
for x in M_over_i[2:]:
    y = isqrt(x)
    temp = N
    for k in range(1, y + 1):
        temp += max(0, min(x // k, N) - x // (k + 1)) * dp[rd[k]] % mod
        temp %= mod
    Last = min(N, x//(y + 1))
    for i in range(Last + 1):
        if i <= 1:
            continue
        temp += dp[rd[x // i]]
        temp %= mod
    dp.append(temp * mother % mod)
print(dp[rd[M]])