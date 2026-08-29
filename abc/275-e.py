def main():
    N,M,K = map(int,input().split())
    dp = [0 for i in range(N+1)]
    mod = 998244353
    ans=0
    chance = (M-1)*pow(M,mod-2,mod)%mod
    deme  = pow(M,mod-2,mod)
    dp[0]=1
    for rem in reversed(range(K)):
        for i in reversed(range(N+1)):
            for me in range(1,M+1):
                if i+me==N:
                    ans+=dp[i]*deme%mod
                    ans%=mod
                elif i+me+M>=N:
                    ans+=(1-pow(chance,rem,mod))%mod*dp[i]%mod*deme%mod
                    ans%=mod
                else:
                    dp[i+me]+=deme*dp[i]%mod
                    dp[i+me]%=mod
            dp[i]=0
    print(ans)
main()
