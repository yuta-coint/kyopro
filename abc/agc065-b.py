mod = 10**9+7
N = int(input())
P = list(map(lambda x:int(x)-1,input().split()))
rp = [0 for i in range(N)]
cnt = [0 for i in range(N)]
for i in range(N):
    rp[P[i]] = sum(cnt[:P[i]])
    cnt[P[i]] = 1
dp = [1 for i in range(N)]
dp_sum = [sum(dp)]
for i in range(N):
    dp_sum.append(dp_sum[-1]-dp[i])
for i in reversed(range(N-1)):
    new_dp = []
    #print(dp_sum)
    for j in range(i+1):
        #print(rp[i],j)
        if rp[i]>=j:
            new_dp.append(dp_sum[j])
        else:
            new_dp.append(dp_sum[j+1])
    dp = new_dp
    dp_sum = [sum(dp)%mod]
    for j in range(i+1):
        dp_sum.append((dp_sum[-1]-dp[j])%mod)
    #print(dp)
print(dp_sum[0])