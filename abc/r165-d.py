import sys
input = sys.stdin.readline
# トポロジカルソートの可否を返す(定数倍が若干マシ)
from typing import List
from collections import deque
def toposort(g: List[List[int]]) -> bool:
    cnt = [0] * len(g)
    for frm in range(len(g)):
        for to in g[frm]:
            cnt[to] += 1
 
    q: deque = deque()
 
    for i, c in enumerate(cnt):
        if c == 0:
            q.append(i)

    while q:
        u = q.pop()
        for v in g[u]:
            cnt[v] -= 1
            if cnt[v] == 0:
                q.append(v)
 
    for c in cnt:
        if c != 0:
            return False
 
    return True
N,M = map(int,input().split())
X = []
pls = [0 for i in range(M)]
point = [0 for i in range(N)]
for i in range(M):
    a,b,c,d = map(int,input().split())
    if a==c:
        if b<d:
            c+=b-a+1
            a=b+1
        else:
            print("No")
            exit()
    X.append((a-1,b,c-1,d))
tree = [i for i in range(N)]
sys.setrecursionlimit(10**6)
def find(i):
    if tree[i] == i:
        return i
    else:
        tree[i]= find(tree[i])
        return find(tree[i])

def union(a,b):
    if tree[a] > tree[b]:
        a,b = b,a
    tree[find(b)] = find(a)


def scc(G):
    rG = [[] for i in range(N)]
    for i in range(N):
        for j in G[i]:
            rG[j].append(i)
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

    unvisited=[True for i in range(N)]
    #帰りがけの番号
    back = [None for i in range(N)]
    global cnt
    cnt = 0
    for i in range(N):
        if unvisited[i]:
            dfs(i)
    unvisited=[True for i in range(N)]
    gro = [None for i in range(N)]
    global group_count
    group_count = 0
    for i in reversed(range(N)):
        if unvisited[back[i]]:
            dfs2(back[i])
            group_count+=1
    return gro

while True:
    G = [[] for _ in range(N)]
    #嘘解法らしい。とりあえずYesがNoになっている。
    #SCCで連結成分全部つぶすか
    for j in range(M):
        a,b,c,d = X[j]
        if a==b:
            continue
        G[find(a)].append(find(c))
    if toposort(G):
        print("Yes")
        exit()
    S = []
    scced = scc(G)
    for a,b,c,d in X:
        if scced[find(a)]==scced[find(c)]:
            union(a,c)
    for j in range(M):
        a,b,c,d = X[j]
        if a==b:
            continue
        if find(a)==find(c):
            if c+1==d:
                print("No")
                exit()
            X[j]=(a+1,b,c+1,d)