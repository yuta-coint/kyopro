def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    N,D  = map(int,input().split())
    D+=1
    mod = 998244353
    ch = []
    s = 1
    for i in range(1,D):
        ch.append(s)
        s*=D-i-1
        s%=mod
        s*=pow(i,mod-2,mod)
        s%=mod
    ch.append(s)
    ans = 2
    for k in range(1,D):
        if k==1 or k==D-1:
            a,b,c,d =0,1,1,D-2
        else:
            a,b,c,d =ch[k-2],ch[k-1],ch[k-1],ch[k]
        pow_a,pow_b,pow_c,pow_d = [],[],[],[]
        for i in range(45):
            pow_a.append(a)
            pow_b.append(b)
            pow_c.append(c)
            pow_d.append(d)
            a,b,c,d = (a*a+b*c)%mod,(a*b+b*d)%mod,(c*a+d*c)%mod,(c*b+d*d)%mod
        a,b,c,d = 1,0,0,1
        for i in range(45):
            if (N>>i)&1:
                e,f,g,h = pow_a[i],pow_b[i],pow_c[i],pow_d[i]
                a,b,c,d = (a*e+b*g)%mod,(a*f+b*h)%mod,(c*e+d*g)%mod,(c*f+d*h)%mod
        ans=(ans+a+d)%mod
    print(ans)
main()