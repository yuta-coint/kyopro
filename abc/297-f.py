H,W,K = map(int,input().split())
mod = 998244353
fac = [1]
for i in range(1,10**6+803):
    fac.append(fac[-1]*i%mod)
temp = fac[-1]
temp = pow(temp,mod-2,mod)
mother = [temp]
for i in reversed(range(1,10**6+803)):
    mother.append(mother[-1]*i%mod)
mother.reverse()
def nck(x):
    if x<K:
        return(0)
    else:
        return(fac[x]*mother[x-K]%mod*mother[K]%mod)
ans = 0
for i in range(H):
    for j in range(W):
        ans+=nck(H*W)-nck(i*W)-nck((H-i-1)*W)-nck(j*H)-nck((W-j-1)*H)
        ans%=mod
        ans+=nck(i*j)+nck(i*(W-j-1))+nck((H-i-1)*j)+nck((H-i-1)*(W-j-1))
        ans%=mod
ans*=pow(nck(H*W),mod-2,mod)
print(ans%mod)