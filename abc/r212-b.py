from heapq import heappush, heappop
INF = 10 ** 24
N, M = map(int,input().split())
V = N
E = M - 1
dist = [INF] * V
G = [[]for i in range(V)]
initial_cost = 0
for i in range(M):
    x, y, c = map(int,input().split())
    if i == 0:
        r = y - 1
        goal = x - 1
        initial_cost = c
    else:
        G[x - 1].append((c, y - 1))
hq = [(0, r)] #(distance, node)
dist[r] = 0
seen = [False] * V # ノードが確定済みかどうか
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    #print(v)
    seen[v] = True
    for i in G[v]: # ノード v に隣接しているノードに対して
        if seen[i[1]] == False and dist[v] + i[0] < dist[i[1]]:
            dist[i[1]] = dist[v] + i[0]
            heappush(hq, (dist[i[1]], i[1]))
    #print(dist)
if dist[goal] == INF:
    print(- 1)
else:
    print(dist[goal] + initial_cost)
