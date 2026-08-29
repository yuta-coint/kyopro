#包除原理は
R,G,B,K = map(int,input().split())
mod=998244353
fac = [1]
for i in range(1,3*(10**6)+1):
    fac.append((fac[-1]*i)%mod)
fac_rev =[pow(fac[-1],mod-2,mod)]
for i in reversed(range(1,3*(10**6)+1)):
    fac_rev.append((fac_rev[-1]*i)%mod)
fac_rev.reverse()
R,G = min(R,G),max(R,G)
def pcq(p,q):
    return(fac[p]*fac_rev[p-q]%mod*fac_rev[q]%mod)
print(pcq(G+B,B)*pcq(G,K)%mod*pcq(B+R,R-K)%mod)
