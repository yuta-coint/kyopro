def main():
    N = int(input())
    a = list(map(int,input().split()))
    mod = 998244353
    ans = 0
    for i in range(1,N+1):
        dp = [[0 for j in range(i)] for k in range(i+1)]
        dp[0][0]=1
        for j in range(N):
            for s in reversed(range(i)):
                for t in range(i):
                    dp[s+1][(t+a[j])%i]+=dp[s][t]
                    dp[s+1][(t+a[j])%i]%=mod
        ans+=dp[i][0]
        ans%=mod
    print(ans)
main()