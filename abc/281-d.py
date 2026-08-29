def main():
    N,K,D = map(int,input().split())
    a = list(map(int,input().split()))
    dp = [[-1 for k in range(D)] for j in range(K)]
    for i in range(N):
        for j in reversed(range(1,K)):
            for k in range(D):
                if dp[j-1][(k-a[i])%D]==-1:
                    continue
                if dp[j][k]<dp[j-1][(k-a[i])%D]+a[i]:
                    dp[j][k]=dp[j-1][(k-a[i])%D]+a[i]
        if dp[0][a[i]%D]<a[i]:
            dp[0][a[i]%D]=a[i]
    print(dp[K-1][0])
main()