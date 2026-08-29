N = int(input())
C = list(input().split())
mod = 10**9+7
G = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
visited = [False for i in range(N)]
dpa = [0 for i in range(N)]
dpb = [0 for i in range(N)]
dpab = [0 for i in range(N)]
for i in range(N):
    if C[i]=="a":
        dpa[i]=1
    else:
        dpb[i]=1
def dfs(v):
    visited[v]=True
    for i in G[v]:
        if visited[i]==False:
            dfs(i)
            pa = dpa[v]*dpab[i]%mod + dpa[v]*dpa[i]%mod
            pb = dpb[v]*dpab[i]%mod + dpb[v]*dpb[i]%mod
            pab = ((dpa[v]+dpb[v]+dpab[v])%mod*dpab[i]%mod+(dpa[i]+dpb[i]+dpab[i])%mod*dpab[v]%mod+dpa[i]*dpb[v]%mod+dpa[v]*dpb[i]%mod)%mod
            #print(v,i,pa,pb,pab)
            dpa[v]=pa
            dpb[v]=pb
            dpab[v] =pab
dfs(0)
print(dpab[0])
