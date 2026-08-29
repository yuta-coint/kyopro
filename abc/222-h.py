mod = 998244353
def n_inv(N):
    r = [-1, 1]
    for i in range(2, N + 1):
        r.append((mod-r[mod % i] * (mod // i)) % mod)
    return r
N= int(input())
ans = [1, 6 * N]
n_inv_list = n_inv(N)
for i in range(2, N + 1):
    res = ((6 * N - 3 * (i - 1)) * ans[i - 1] % mod + (4 * N - i + 2) * ans[i - 2] % mod)% mod
    res *= n_inv_list[i]
    res %= mod
    ans.append(res)
print(ans[N - 1] * n_inv_list[N] % mod)
