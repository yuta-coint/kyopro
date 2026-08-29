N,S = map(int,input().split())
A  = list(map(int,input().split()))
mod = 998244353
dp = [0 for j in range(S+1)]
ans = []
for i in range(N):
    if A[i]>S:
        ans.append(dp[S])
        continue
    for j in reversed(range(A[i]+1,S+1)):
        dp[j]+=dp[j-A[i]]
        dp[j]%=mod
    dp[A[i]]+=i+1
    dp[A[i]]%=mod
    ans.append(dp[S])
#print(ans)
print(sum(ans)%mod)
        
