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
distance_Sum = [0 for i in range(N)]
distance_Zero = [0 for i in range(N)]
unvisited = [True for i in range(N)]
def bfsdj(v):
    unvisited[v]=False
    for i in G[v]:
        if unvisited[i]:
            distance_Zero[i] = distance_Zero[v]+1
            bfsdj(i)
bfsdj(0)
distance_Sum[0] = sum(distance_Zero)
unvisited = [True for i in range(N)]
def DS(v):
    unvisited[v]=False
    for i in G[v]:
        if unvisited[i]:
            distance_Sum[i] = distance_Sum[v]-subtree_size[i]*2+N
            DS(i)
DS(0)
for i in range(N):
    print(distance_Sum[i])
