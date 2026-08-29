#トポロジカルソートする
from typing import List
def TopologicalSort(G,N):
    ans = [0 for i in range(N)]
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
            if ans[i]<ans[n]+1:
                ans[i]=ans[n]+1
            inedge[i] -= 1
            if inedge[i] == 0:
                S.append(i)
    if max(inedge)==0:
        return(max(ans))
    else:
        return(-1)
N,M = map(int,input().split())
G = [[] for i in range(N)]
rG = [[] for i in range(N)]
for i in range(M):
    x,y = map(int,input().split())
    G[x-1].append(y-1)
print(TopologicalSort(G,N))

