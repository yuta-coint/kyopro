n = int(input())
mod  =998244353
k  = len(str(n))
pow10 =9
repu9 = 1
ans = 0
for i in range(k-1):
    ans+=((pow10)*(pow10+1)//2)%mod
    ans%=mod
    pow10*=10
    pow10%=mod
    repu9*=10
    repu9%=mod
ans+=((n-repu9+1)*(n-repu9+2)//2)%mod
ans%=mod
print(ans)

