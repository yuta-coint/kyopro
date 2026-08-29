#トポロジカルソートする
from typing import List
def TopologicalSort(G,N):
    inedge = [0]*N
    for frm in range(N):
        for to in G[frm]:
            inedge[to]+=1
    L = []
    from collections import deque
    S = deque()
    for i in range(N):
        if inedge[i]==0:
            S.append(i)
    while S:
        n = S.popleft()
        L.append(n)
        for i in G[n]:
            inedge[i] -= 1
            if inedge[i] == 0:
                S.append(i)
    if max(inedge)==0:
        return(L)
    else:
        return(-1)


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