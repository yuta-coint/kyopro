from collections import deque
INF = 10 ** 9
N1,N2,M = map(int,input().split())
dist = [float("inf")] * (N1+N2)
G = [[]for i in range(N1+N2)]
hq = deque()
hq.append(0)
hq.append(N1+N2-1)
 #(distance, node)
dist[0] = 0
dist[N1+N2-1]=0
seen = [False] * (N1+N2) # ノードが確定済みかどうか
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
while hq:
    v = hq.popleft() # ノードを pop する
    if seen[v]:
        continue
    #print(v)
    seen[v] = True
    for i in G[v]: # ノード v に隣接しているノードに対して
        if seen[i] == False and dist[v] + 1 < dist[i]:
            dist[i] = dist[v] + 1
            hq.append(i)
    #print(dist)
print(max(dist[:N1])+max(dist[N1:])+1)
def bfs_dj(G,r):
    from collections import deque
    INF = 10 ** 9
    N1,N2,M = map(int,input().split())
    dist = [float("inf")] * (N1+N2)
    hq = deque()
    #スタートが複数あるならこの辺をいじる
    hq.append(r)
    #(distance, node)
    dist[r] = 0
    seen = [False] * (N1+N2) # ノードが確定済みかどうか
    while hq:
        v = hq.popleft() # ノードを pop する
        if seen[v]:
            continue
        #print(v)
        seen[v] = True
        for i in G[v]: # ノード v に隣接しているノードに対して
            if seen[i] == False and dist[v] + 1 < dist[i]:
                dist[i] = dist[v] + 1
                hq.append(i)
        #print(dist)
    return dist
