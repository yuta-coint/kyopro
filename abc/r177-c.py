N = int(input())
c = [list(input()) for i in range(N)]
from collections import deque
ans = 0
visited = [False for i in range(N*N)]
dist = [10**9 for i in range(N*N)]
q = deque()
q.append(0)
dist[0]=0
while q:
    v = q.popleft()
    if visited[v]:
        continue
    visited[v] = True
    next = []
    #隣接する点を列挙
    if v%N!=0:
        next.append(v-1)
    if v%N!=N-1:
        next.append(v+1)
    if v//N!=0:
        next.append(v-N)
    if v//N!=N-1:
        next.append(v+N)
    for e in next:
        if visited[e]:
            continue
        #距離が0
        if c[v//N][v%N]=="R":
            if dist[e]>dist[v]:
                dist[e]=dist[v]
                q.appendleft(e)
        #
        else:
            if dist[e]>dist[v]+1:
                dist[e]=dist[v]+1
                q.append(e)
ans += dist[N*N-1]
visited = [False for i in range(N*N)]
dist = [10**9 for i in range(N*N)]
q = deque()
q.append(N-1)
dist[N-1]=0
while q:
    v = q.popleft()
    if visited[v]:
        continue
    visited[v] = True
    next = []
    if v%N!=0:
        next.append(v-1)
    if v%N!=N-1:
        next.append(v+1)
    if v//N!=0:
        next.append(v-N)
    if v//N!=N-1:
        next.append(v+N)
    for e in next:
        if visited[e]:
            continue
        if c[v//N][v%N]=="B":
            if dist[e]>dist[v]:
                dist[e]=dist[v]
                q.appendleft(e)
        else:
            if dist[e]>dist[v]+1:
                dist[e]=dist[v]+1
                q.append(e)
ans += dist[N*N-N]
print(ans)