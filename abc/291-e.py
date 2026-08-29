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
    lenS = 0
    for i in range(N):
        if inedge[i]==0:
            S.append(i)
            lenS+=1
    while S:
        if lenS>1:
            return(-1)
        n = S.popleft()
        lenS-=1
        L.append(n)
        for i in G[n]:
            inedge[i] -= 1
            if inedge[i] == 0:
                S.append(i)
                lenS+=1
    if max(inedge)==0:
        return(L)
    else:
        return(-1)

N,M = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    x,y = map(int,input().split())
    G[x-1].append(y-1)
ans = TopologicalSort(G,N)
if ans==-1:
    print("No")
else:
    ansr = [0 for i in range(N)]
    for i in range(N):
        ansr[ans[i]]=i+1
    print("Yes")
    print(*ansr)