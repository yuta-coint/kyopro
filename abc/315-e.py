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
N=  int(input())
P = [[]]
for i in range(N):
    c,*p = list(map(int,input().split()))
    P.append(p)
from collections import deque
q = deque()
q.append(1)
read = [0 for i in range(N+1)]
while q:
    v = q.popleft()
    if read[v]==1:
        continue
    read[v]=1
    for i in P[v]:
        q.append(i)
G = [[] for i in range(N+1)]
for i in range(N+1):
    if read[i]==0:
        continue
    for j in P[i]:
        if read[j]==0:
            continue
        G[j].append(i)
ans = []
bigans = TopologicalSort(G,N+1)
for i in range(N+1):
    if read[bigans[i]]==0:
        continue
    ans.append(bigans[i])
print(*ans)
