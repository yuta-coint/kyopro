N,K = map(int,input().split())
A = list(map(int,input().split()))
dp = [0 for i in range(N+1)]
for i in range(1,N+1):
    #dp[i-j]は相手が取れる個数なのでこれをiから引く
    for j in A:
        if i-j<0:
            continue
        if i-dp[i-j]>dp[i]:
            dp[i]=i-dp[i-j]
print(dp[N])