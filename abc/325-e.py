from heapq import heappush, heappop
INF = 10 ** 24
N,A,B,C = map(int,input().split())
adj = [list(map(int,input().split())) for i in range(N)]
dist1 = [INF] * N
dist2 = [INF] * N
hq = [(0, 0)] #(distance, node)
dist1[0] = 0
seen = [False] * N # ノードが確定済みかどうか
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    #print(v)
    seen[v] = True
    for i in range(N): # ノード v に隣接しているノードに対して
        if i==v:
            continue
        if seen[i] == False and dist1[v] + adj[i][v]*A < dist1[i]:
            dist1[i] = dist1[v] + adj[i][v]*A
            heappush(hq, (dist1[i], i))
    #print(dist)
hq = [(0, N-1)] #(distance, node)
dist2[N-1] = 0
seen = [False] * N # ノードが確定済みかどうか
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    #print(v)
    seen[v] = True
    for i in range(N): # ノード v に隣接しているノードに対して
        if i==v:
            continue
        if seen[i] == False and dist2[v] + adj[i][v]*B + C < dist2[i]:
            dist2[i] = dist2[v] + adj[i][v]*B + C
            heappush(hq, (dist2[i], i))
    #print(dist)
ans = INF
for i in range(N):
    if ans>dist1[i]+dist2[i]:
        ans = dist1[i]+dist2[i]
print(ans)