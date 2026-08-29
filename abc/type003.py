import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
G = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
def dfs(i):
    visited[i] = True
    for v in G[i]:
        if visited[v]==False:
            d[v] = d[i]+1
            dfs(v)
visited = [False for i in range(n)]
d = [0 for i in range(n)]
dfs(0)
k = d.index(max(d))
visited = [False for i in range(n)]
d = [0 for i in range(n)]
dfs(k)
print(max(d))
