import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
V,E = map(int,input().split())
G = [[] for i in range(V)]
rG = [[] for i in range(V)]
for i in range(E):
    s,t = map(int,input().split())
    G[s].append(t)
    rG[t].append(s)
def dfs(v):
    global cnt
    unvisited[v] = False
    for i in G[v]:
        if unvisited[i]:
            dfs(i)
    back[cnt]=v
    cnt+=1
def dfs2(v):
    global group_count
    unvisited[v] = False
    gro[v] = group_count
    for i in rG[v]:
        if unvisited[i]:
            dfs2(i)

unvisited=[True for i in range(V)]
#帰りがけの番号
back = [None for i in range(V)]
cnt = 0
for i in range(V):
    if unvisited[i]:
        dfs(i)
unvisited=[True for i in range(V)]
gro = [None for i in range(V)]
group_count = 0
for i in reversed(range(V)):
    if unvisited[back[i]]:
        dfs2(back[i])
        group_count+=1
q = int(input())
for i in range(q):
    u,v = map(int,input().split())
    if gro[u]==gro[v]:
        print(1)
    else:
        print(0)