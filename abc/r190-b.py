import sys
sys.setrecursionlimit(10**7)
mod =  998244353
#a番目がk以下を求める。
N,a,b = map(int,input().split())
fac = [1]
pow2 = [1]
for i in range(1,10**7+1):
    fac.append(fac[-1]*i%mod)
fac_rev = [pow(fac[-1],-1,mod)]
for i in reversed(range(1,10**7+1)):
    fac_rev.append(fac_rev[-1]*i%mod)
fac_rev.reverse()
def sct(s,t):
    if t<0 or s-t<0:
        return 0
    else:
        return fac[s]*fac_rev[t]%mod*fac_rev[s-t]%mod
calca = [0]
calcb = [0]
for k in range(1,N+1):
    calca.append((calca[-1]+sct(N-k,a-1)+sct(N-k,a-k))%mod*499122177%mod)
    calcb.append((calcb[-1]+sct(N-k,b-1)+sct(N-k,b-k))%mod*499122177%mod)
#print(calca)
#print(calcb)
Q = int(input())
ks = list(map(int,input().split()))
ans = 0
for k in ks:
    ans = calca[k]*calcb[k]%mod*pow(2,2*k-2,mod)%mod - calca[k-1]*calcb[k-1]%mod*pow(2,2*k-4,mod)%mod
    print(ans%mod)
    #ans %=mod
#print(pow(4,N-1,mod))
#print(calc(a,N)*calc(b,N)%mod)