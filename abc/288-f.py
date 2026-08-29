mod = 998244353
N=int(input())
X = list(input())
ans = [int(X[0])]
ans_sum = [1,1+ans[-1]]
for i in range(1,N):
    d = int(X[i])
    ans.append((ans[i-1]*(10+d)%mod+ans_sum[i-1]*d%mod)%mod)
    ans_sum.append((ans[-1]+ans_sum[-1])%mod)
print(ans)
print(ans[-1])
