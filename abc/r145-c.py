N = int(input())
mod = 998244353
ans = 1
mother = N+1
for i in range(1,N+1):
    ans*=2
    ans%=mod
    ans*=i
    ans%=mod
    ans*=N+i
    ans%=mod
    mother*=i
    mother%=mod
ans *= pow(mother,mod-2,mod)
ans%=mod
print(ans)