#https://tjkendev.github.io/procon-library/python/range_query/rsq_raq_bit.html
import sys
readline = sys.stdin.readline
write = sys.stdout.write
N, Q = map(int, readline().split())

mod = 998244353
data0 = [0]*(N+1)
data1 = [0]*(N+1)
data2 = [0]*(N+1)
data3 = [0]*(N+1)
def _add(data, k, x):
    while k <= N:
        data[k] += x
        data[k] %= mod
        k += k & -k
def add(l, r, x):
    _add(data0, l, -x*(l-1)%mod)
    _add(data0, r, x*(r-1)%mod)
    _add(data1, l, x)
    _add(data1, r, -x)
    _add(data2, l, -x*x*(l-1)%mod)
    _add(data2, r, x*x*(r-1)%mod)
    _add(data3, l, x*x%mod)
    _add(data3, r, -x*x%mod)

def _get(data, k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
        s %= mod
    return s
def query(l, r):
    ans = _get(data1, r-1) * (r-1) + _get(data0, r-1) - _get(data1, l-1) * (l-1) - _get(data0, l-1)
    ans %= mod
    ans = ans * ans % mod
    ans2 = _get(data3, r-1) * (r-1) + _get(data2, r-1) - _get(data3, l-1) * (l-1) - _get(data2, l-1)
    print(ans,ans2)
    ans -= ans2
    ans %= mod
    ans *= 499122177
    ans %= mod
    return ans

for q in range(Q):
    l,r,a = map(int,input().split())
    add(l,r + 1,a)
    print(query(l,r + 1))