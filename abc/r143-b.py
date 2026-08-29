def main():
    mod = 998244353
    N = int(input())
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
    temp = 1
    for i in range(1,N*N+1):
        temp*=i
        temp%=mod
    rr = pcq(N*N,2*N-1)
    k=1
    for i in range(1,N):
        k*=i
        k%=mod
    L = 1
    for i in range(1,N*N-2*N+2):
        L*=i
        L%=mod
    rr*=k
    rr%=mod
    rr*=k
    rr%=mod
    rr*=N*N
    rr%=mod
    rr*=L
    rr%=mod
    print((temp-rr)%mod)
main()
