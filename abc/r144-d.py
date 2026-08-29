N,K = map(int,input().split())
mod = 998244353
##mの(pow乗)
def bigpower(base,pow):
    num = 1
    for i in reversed(range(len(bin(pow)))):
        num = num*num%mod
        if pow>>i & 1:
            num = num*base%mod
        i+=1
    return(num)

###組み合わせをmodで割った余り（pCq、計算量pq）
def pcq(p,q):
    com = 1
    for i in range(q):
        com *= bigpower(i+1,mod-2)
        com *= p-i
        com %= mod
    return(com)
##Ncnを計算するやつ
Ncn = []
c = 1
for i in range(N):
    Ncn.append(c)
    c *= bigpower(i+1,mod-2)
    c *= N-i
    c %= mod
Ncn.append(c)
#nの階乗
nper = []
t = 1
for i in range(1,2*N+2):
    nper.append(t)
    t*=i
    t%=mod
#####################
if K>=N:
    #(k+n)!/(K-N+n)!を計算する
    k_plus_n_per = []
    t = 1
    for i in range(K-N+1,K+1):
        t*=i
        t%=mod
    k_plus_n_per.append(t)
    for i in range(1,N+1):
        t*=K+i
        t%=mod
        t*=bigpower(K-N+i,mod-2)
        t%=mod
        k_plus_n_per.append(t)    
    ans = 0
    for n in range(N+1):
        temp = n+K+1
        temp*=bigpower(N+1,mod-2)
        temp%=mod
        temp*=k_plus_n_per[n]
        temp%=mod
        temp*=bigpower((nper[N-n]*nper[n])%mod,mod-2)
        temp%=mod
        temp*=Ncn[n]
        temp%=mod
        ans+=temp
        ans%=mod
else:
    ans = 0
    for n in range(N-K,N+1):
        temp = n+K+1
        temp*=bigpower(N+1,mod-2)
        temp%=mod
        temp*=nper[K+n]
        temp%=mod
        temp*=nper[K-N+n]
        temp%=mod
        temp*=bigpower(K-N+n,mod-2)
        temp%=mod
        temp*=bigpower((nper[N-n]*nper[n])%mod,mod-2)
        temp%=mod
        temp*=Ncn[n]
        temp%=mod
        ans+=temp
        ans%=mod
print(ans)