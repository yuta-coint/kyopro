n,L = map(int,input().split())
ans = [0 for i in range(n+1)]
mod = 10**9+7
if L<=n:
    for i in range(L):
        ans[i]=1
    for i in range(L,n+1):
        ans[i]=(ans[i-1]+ans[i-L])%mod
    print(ans[n])
else:
    print(1)