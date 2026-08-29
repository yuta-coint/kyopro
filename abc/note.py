mod = 998244353
N,K = map(int,input().split())
from collections import defaultdict
from math import gcd
ans = [defaultdict(int) for i in range(N+1)]
ans[0]={1:1}
for i in range(1,N+1):
    #i番目が長さjのサイクルに含まれている
    for j in range(1,i+1):
        cyc = 1
        pre = ans[i-j]
        for k in range(1,j):
            cyc*=i-k
            cyc%=mod
        for k in pre:
            if pre[k]!=0:
                ans[i][k*j//gcd(k,j)]+=pre[k]*cyc%mod
                ans[i][k*j//gcd(k,j)]%=mod
ans_sum = 0
for k in ans[N]:
    #print(k,ans[N][k])
    ans_sum+=ans[N][k]*pow(k,K,mod)%mod
    ans_sum%=mod
print(ans_sum)