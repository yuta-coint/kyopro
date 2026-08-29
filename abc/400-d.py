H,W = map(int,input().split())
S = [["#" for i in range(W+2)]]+[["#"]+list(input())+["#"] for i in range(H)]+[["#" for i in range(W+2)]]
A,B ,C,D = map(int,input().split())
from collections import deque
dq = deque()
dq.append((A,B))
dist = [[10**9 for i in range(W+2)] for j in range(H+2)]
dist[A][B] = 0
visited = [[False for i in range(W+2)] for j in range(H+2)]
while dq:
    p,q = dq.popleft()
    if p<=0 or q<=0 or p>=H+1 or q>=H+1:
        continue
    if visited[p][q]:
        continue
    visited[p][q] = True
    for s,t in [(p-1,q),(p+1,q),(p,q+1),(p,q-1)]:
        if 0<s<H+2 and 0<t<W+2:
            if S[s][t]==".":
                if dist[s][t]>dist[p][q]:
                    dist[s][t]=dist[p][q]
                    dq.appendleft((s,t))
            else:
                if dist[s][t]>dist[p][q]+1:
                    dist[s][t]=dist[p][q]+1
                    dq.append((s,t))
    for s,t in [(p-2,q),(p+2,q),(p,q+2),(p,q-2)]:
        if 0<s<H+2 and 0<t<W+2:
            if dist[s][t]>dist[p][q]+1:
                dist[s][t]=dist[p][q]+1
                dq.append((s,t))
print(dist[C][D])