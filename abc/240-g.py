def main():
    N,x,y,z = map(int,input().split())
    rem  = N-abs(x)-abs(y)-abs(z)
    mod = 998244353
    if rem<0 or rem&1:
        print(0)
        exit()
    x,y,z = abs(x),abs(y),abs(z)
    rem//=2
    ans = 0
    #NC2*k+z 2k+zCk 2*rem+x+y-2*kCR-k 2*rem+x+y-2*kCR-k+xの積を全部足し合わせる
    p=1
    #orはどっちもカウントされることが或るんだよ！
    def combination_count(s,t):
        cnt=1
        fac = 1
        for i in range(1,1+s+t):
            fac*=i
            fac%=mod
            if i==s:
                cnt*=pow(fac,mod-2,mod)
                cnt%=mod
            if i==t:
                cnt*=pow(fac,mod-2,mod)
                cnt%=mod
        cnt*=fac
        cnt%=mod
        return(cnt)
    ans=p=combination_count(N-z,z)*combination_count(rem,rem+x+y)%mod*combination_count(rem+x,rem+y)%mod
    #二項係数って逆からかけていったらlogをとれるのか…
    q=1
    for k in range(1,rem+1):
        q*=k*(k+z)%mod*(2*rem+x+y-2*k+2)%mod*(2*rem+x+y-2*k+1)%mod*(2*rem+x+y-2*k+2)%mod*(2*rem+x+y-2*k+1)%mod
        q%=mod
    q = pow(q,mod-2,mod)
    q_rev = [0 for i in range(rem+1)]
    for k in reversed(range(1,rem+1)):
        q_rev[k]=q
        q*=k*(k+z)%mod*(2*rem+x+y-2*k+2)%mod*(2*rem+x+y-2*k+1)%mod*(2*rem+x+y-2*k+2)%mod*(2*rem+x+y-2*k+1)%mod
        q%=mod
    for k in range(1,rem+1):
        p*=(N+1-2*k-z)*(N+2-2*k-z)%mod*(rem-k+1)%mod*(rem+x+y-k+1)%mod*(rem+x-k+1)%mod*(rem+y-k+1)%mod
        p%=mod
        ans+=(p*q_rev[k])%mod
        ans%=mod
    print(ans)
main()