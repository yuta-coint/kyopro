K = int(input())
mod = 998244353
ans = 0
all_ = K
for i in range(1,6):
    all_ *= K - i
    all_ %= mod
    all_ *= pow(i, -1, mod)
    all_ %= mod

for i in range(K - 3):
    for j in range(K - 3 - i):
        k = K - 3 - j - i
        ans += i * j * k *(max(i,j,k) + 1) % mod
        ans %= mod
print((all_-ans)%mod)