import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,Q = map(int,input().split())
x = list(map(int,input().split()))
G = [[] for i in range(N)]
for i in range(N-1):
    u,v = map(lambda x:int(x)-1,input().split())
    G[u].append(v)
    G[v].append(u)
def dfs(v):
    global subtree_rank
    unvisited[v]=False
    for i in G[v]:
        if unvisited[i]:
            dfs(i)
            subtree_rank[v]+=subtree_rank[i]
            subtree_size[v]+=subtree_size[i]
    subtree_rank[v].sort(reverse=True)
    if subtree_size[v]>20:
        subtree_rank[v] = subtree_rank[v][:20]
unvisited = [True for i in range(N)]
subtree_size = [1 for i in range(N)]
subtree_rank=[[x[i]] for i in range(N)]
dfs(0)
for i in range(Q):
    v,k = map(lambda x:int(x)-1,input().split())
    print(subtree_rank[v][k])

