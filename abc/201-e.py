import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
G = [{} for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    G[u-1][v-1]=w
    G[v-1][u-1]=w
black = [0 for i in range(60)]
white = [0 for i in range(60)]
visited = [False for i in range(N)]
def dfs(v,weight):
    visited[v]=True
    for bit in range(60):
        if (weight>>bit)&1:
            black[bit]+=1
        else:
            white[bit]+=1
    for i in G[v]:
        if visited[i]:
            continue
        dfs(i,weight^G[v][i])
dfs(0,0)
ans = 0
mod = 10**9+7
for i in range(60):
    ans+=pow(2,i,mod)*black[i]%mod*white[i]%mod
    ans%=mod
print(ans)
    
