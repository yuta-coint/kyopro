mod = 998244353
N,M = map(int,input().split())
ab = [tuple(map(int,input().split())) for i in range(N)]
#分母計算パート
F = []
for bits in range(1<<N):
    ind = 0
    base = 1
    for i in range(N):
        if (bits>>i)&1:
            ind+=ab[i][1]+1
            base*=-pow(ab[i][0],ab[i][1]+1,mod)
            base%=mod
    F.append((ind,base))
#(x-a_i)^{-1}の積のx^Mの係数を求める関数
def partial_fraction_decomposition(a,N,m):
    r = 0
    for i in range(N):
        temp = 1
        for j in range(N):
            if i==j:
                continue
            temp *= a[i]-a[j]
            temp %= mod
        temp = pow(temp,mod-2,mod)
        temp *= pow(a[i],mod-m-2,mod)
        temp = mod-temp
        r+=temp
        r%=mod
    return r
c = 1
for i in range(N):
    c*=ab[i][0]
    c%=mod
c = pow(c,mod-2,mod)
if N&1:
    c=mod-c
ans = 0
a = [pow(ab[i][0],mod-2,mod) for i in range(N)]
for ind,base in F:
    if ind>M:
        continue
    ans += partial_fraction_decomposition(a,N,M-ind)*base%mod
    ans %= mod
print(ans*c%mod)