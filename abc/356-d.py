N,M = map(int,input().split())
N+=1
ans = 0
mod = 998244353
for i in range(62):
    if (M>>i)&1:
        syo = N//(1<<(i+1))
        amari =  N%(1<<(i+1))
        ans += syo*(1<<i)%mod
        ans%=mod
        if amari>=(1<<i):
            ans+=amari-(1<<i)
            ans%=mod
print(ans)