from copy import copy
n,K = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
mod = 998244353
pq = [[p[i],q[i]] for i in range(n)]
pq.sort()
q = [pq[i][1]-1 for i in range(n)]
ans = [[0 for k in range(n+1)] for j in range(n+1)]
#ｊ個取っていないものがあり、その中での最大値はｋである。
for i in range(n):
    temp = [[0 for k in range(n+1)] for j in range(n+1)]
    temp[1][q[i]]+=1
    for j in range(1,n):
        for k in range(n):
            if q[i]<k:
                temp[j][k]+=ans[j][k]
                temp[j][k]%=mod
            temp[j+1][min(k,q[i])]+=ans[j][k]
            temp[j+1][min(k,q[i])]%=mod
    ans = copy(temp)
#print(ans)
allget = 0
if K==n:
    allget = 1
print((sum(ans[n-K])+allget)%mod)