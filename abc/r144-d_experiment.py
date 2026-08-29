def main():
    N,K = map(int,input().split())
    mod = 998244353
    ##mの(pow乗)
    bp = [pow(i,mod-2,mod) for i in range(2*N+2)]
    ##Ncnを計算するやつ
    Ncn = []
    c = 1
    for i in range(N):
        Ncn.append(c)
        c *= bp[i+1]
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
    #K+n+1Cm
    if K>=N:
        Mcn = []
        c = pow(nper[N+1],mod-2,mod)
        for i in range(K+1-N,K+2):
            c = c*i%mod
        for n in range(1,N+1):
            Mcn.append(c)
            c=c*(K+n+1)%mod
            c=c*pow(K+n-N,mod-2,mod)
            c%=mod
        Mcn.append(c)
        ans = 0
        for n in range(N+1):
            ans+=Ncn[n]*Mcn[n]%mod
            ans%=mod
    else:
        ans = 0
        for n in range(N+1):
            if K+n+1<N+1:
                continue
            M=pow(nper[K+n-N]*nper[N+1],mod-2,mod)
            M*=nper[K+n+1]
            M%=mod
            ans+=Ncn[n]*M%mod
            ans%=mod
    print(ans)
main()
