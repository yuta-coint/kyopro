#(P+1)^K通りのdpをすればいい
N,K,P = map(int,input().split())
dp = [10**24 for i in range((P+1)**K)]
dp[0] = 0
for i in range(N):
    C,*A = list(map(int,input().split()))
    for effect in reversed(range(1,(P+1)**K)):
        cond = []
        temp = effect
        for j in range(K):
            cond.append(temp%(P+1))
            temp//=(P+1)
        pre = 0
        for j in range(K):
            if A[j]<cond[j]:
                pre+=(cond[j]-A[j])*((P+1)**j)
        if dp[pre]+C<dp[effect]:
            dp[effect]=dp[pre]+C
        for j in range(K):
            if cond[j]<P:
                if dp[effect+(P+1)**j]<dp[effect]:
                    dp[effect] = dp[effect+(P+1)**j]
if dp[-1]==10**24:
    print(-1)
else:
    print(dp[-1])