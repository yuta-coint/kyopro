import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    u,v = map(lambda x:int(x)-1,input().split())
    G[u].append(v)
    G[v].append(u)
def dfs(v):
    unvisited[v]=False
    for i in G[v]:
        if unvisited[i]:
            dfs(i)
            subtree_size[v]+=subtree_size[i]
unvisited = [True for i in range(N)]
subtree_size = [1 for i in range(N)]
dfs(0)
ans = 0
for i in range(1,N):
    ans+=subtree_size[i]*(N-subtree_size[i])
print(ans)
