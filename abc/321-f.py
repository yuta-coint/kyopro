mod = 998244353
Q,K = map(int,input().split())
dp = [0 for i in range(K+1)]
dp[0]=1
for _ in range(Q):
    sgn,x = input().split()
    x = int(x)
    if sgn == "+":
        for i in reversed(range(x,K+1)):
            dp[i]+=dp[i-x]
            dp[i]%=mod
    else:
        for i in range(x,K+1):
            dp[i]-=dp[i-x]
            dp[i]%=mod
    print(dp[K])