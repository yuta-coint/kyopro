import sys
input = sys.stdin.readline
mod = 998244353
n,m,k = map(int,input().split())
danger = []
for i in range(m):
    u,v=map(int,input().split())
    danger.append([u-1,v-1])
ans = [0 for i in range(n)]
ans[0] = 1
for i in range(k):
    sa = sum(ans)%mod
    newans = [(sa-ans[i])%mod for i in range(n)]
    for ed in danger:
        newans[ed[0]]-=ans[ed[1]]
        newans[ed[1]]-=ans[ed[0]]
        newans[ed[0]]%=mod
        newans[ed[1]]%=mod
    ans = newans
print(newans[0])
