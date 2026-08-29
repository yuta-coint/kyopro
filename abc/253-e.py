N,M,K = map(int,input().split())
mod =998244353
#最後がi
dp = [1 for i in range(M)]
for i in range(N-1):
    dpsum = [0 for j in range(M+1)]
    for j in range(1,M+1):
        dpsum[j]=(dpsum[j-1]+dp[j-1])%mod
    #print(dpsum)
    for j in range(M):
        if K==0:
            dp[j]=dpsum[M]
        else:
            dp[j] = (dpsum[M]-dpsum[min(j+K,M)]+dpsum[max(j-K+1,0)])%mod
print(sum(dp)%mod)