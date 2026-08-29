import sys
input = sys.stdin.readline
from heapq import heappush, heappop
INF = 10 ** 9
V,E = map(int,input().split())
dist = [INF] * V
G = [[]for i in range(V)]
hq = [(0, 0)] #(distance, node)
dist[0] = 0
seen = [False] * V # ノードが確定済みかどうか
for i in range(E):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    G[a].append([c,b])
    G[b].append([c,a])
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    #print(v)
    seen[v] = True
    for i in G[v]: # ノード v に隣接しているノードに対して
        if seen[i[1]] == False and dist[v] + i[0] < dist[i[1]]:
            dist[i[1]] = dist[v] + i[0]
            heappush(hq, (dist[i[1]], i[1]))
    #print(dist)
dist2 = [INF] * V
hq = [(0, V-1)] #(distance, node)
dist2[V-1] = 0
seen = [False] * V # ノードが確定済みかどうか
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    #print(v)
    seen[v] = True
    for i in G[v]: # ノード v に隣接しているノードに対して
        if seen[i[1]] == False and dist2[v] + i[0] < dist2[i[1]]:
            dist2[i[1]] = dist2[v] + i[0]
            heappush(hq, (dist2[i[1]], i[1]))
    #print(dist)
for i in range(V):
    print(dist[i]+dist2[i])
