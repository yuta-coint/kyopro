import sys
from tokenize import group
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
V,E = map(int,input().split())
G = [[] for i in range(V)]
rG = [[] for i in range(V)]
for i in range(E):
    s,t = map(lambda x:int(x)-1,input().split())
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
    global member_count
    member_count+=1
    unvisited[v] = False
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
ans = 0
for i in reversed(range(V)):
    member_count = 0
    if unvisited[back[i]]:
        dfs2(back[i])
        ans+=member_count*(member_count-1)//2
print(ans)