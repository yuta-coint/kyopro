mod = 998244353
N,K = map(int,input().split())
#自分より小さいやつがあれば一つだけ連絡できる。
#自分より小さいやつが両側にある時、その二つがKより離れているなら両方と連絡できる。
fac = [1]
for i in range(1,10**6):
    fac.append(fac[-1]*i%mod)
fac_inv = [pow(fac[-1],mod-2,mod)]
for i in reversed(range(1,10**6)):
    fac_inv.append(fac_inv[-1]*i%mod)
fac_inv.reverse()


N_inv = pow(N,mod-2,mod)
pt = []
for t in range(N):
    zero = 0
    for i in range(N):
        L = min(i,K)+min(N-1-i,K)
        if N-L-1-t>=0:
            zero += fac[N-L-1]*fac[N-1-t]%mod*fac_inv[N-L-1-t]%mod
            zero%=mod
    two = 0
    if t>=2:
        for k in range(1,K+1):
            if N-K-k-1>=t-2:
                two+=fac[N-k-K]*fac[N-t-1]%mod*t*(t-1)%mod*(K+1-k)%mod*fac_inv[N-K-k-t+1]%mod
                two%=mod
    one = fac[N]-zero-two
    pt.append((one+two*2)%mod)
print(pt)
A = list(map(int,input().split()))
A.sort()
ans = 0
for i in range(N):
    ans += A[i]*pt[i]%mod
    ans %= mod
print(ans)