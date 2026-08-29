mod = 998244353
N,K,L = map(int,input().split())
if L<N-K+1:
    print(0)
    exit()
ans = 1
for i in range(N):
    if i<N-K:
        ans*=L-i
    else:
        ans*=L-N+K
    ans %= mod
print(ans)