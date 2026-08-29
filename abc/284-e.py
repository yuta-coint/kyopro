N,M = map(int,input().split())
import sys
input = sys.stdin.readline
sys.setrecursionlimit(3*(10**6))
G = [[] for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
ans = 0
have = [False for i in range(N)]
def dfs(v):
    global ans
    ans+=1
    if ans>=10**6:
        print(10**6)
        exit()
    have[v]=True
    for i in G[v]:
        if have[i]:
            continue
        dfs(i)
    have[v]=False
dfs(0)
print(ans)
