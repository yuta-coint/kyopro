#累積和を用いてdpする
N,K = map(int,input().split())
a = list(map(int,input().split()))
ans = [0 for i in range(K+1)]
ans_sum = [1 for i in range(K+1)]
ans[0]=1
mod = 10**9+7
for i in range(N):
    for candies in reversed(range(K+1)):
        if candies<=a[i]:
            ans[candies]=ans_sum[candies]
        else:
            ans[candies]=(ans_sum[candies]-ans_sum[candies-a[i]-1])%mod
    for i in range(1,K+1):
        ans_sum[i]=(ans_sum[i-1]+ans[i])%mod
print(ans[K])
