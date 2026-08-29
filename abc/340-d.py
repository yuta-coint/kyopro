from heapq import heappush, heappop
INF = 10 ** 9
N = int(input())
V = N
dist = [float("inf")] * V
G = [[]for i in range(V)]
hq = [(0, 0)] #(distance, node)
dist[0] = 0
seen = [False] * V # ノードが確定済みかどうか
for i in range(N-1):
    a,b,x = map(int,input().split())
    G[i].append((a,i+1))
    G[i].append((b,x-1))
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    if seen[v]:
        continue
    #print(v)
    seen[v] = True
    for i in G[v]: # ノード v に隣接しているノードに対して
        if seen[i[1]] == False and dist[v] + i[0] < dist[i[1]]:
            dist[i[1]] = dist[v] + i[0]
            heappush(hq, (dist[i[1]], i[1]))
    #print(dist)
print(dist[N-1])