import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
ansl = [N for i in range(N)]
ansr = [0 for i in range(N)]
cnt = 0
unvisited = [True for i in range(N)]
root = [True for i in range(N)]
def dfs(v):
    global cnt
    global ansl
    global ansr
    unvisited[v]= False
    for i in G[v]:
        if unvisited[i]:
            dfs(i)
            ansl[v] = min(ansl[v],ansl[i])
            ansr[v] = max(ansr[v],ansr[i])
            root[v] = False
    if root[v]:
        ansl[v] = cnt
        ansr[v] = cnt
        cnt+=1
dfs(0)
for i in range(N):
    print(ansl[i]+1,ansr[i]+1)





