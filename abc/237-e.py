from heapq import heappush, heappop
import sys
input  = sys.stdin.readline
INF = float("inf")
V,E= map(int,input().split())
r = 0
dist = [INF] * V
G = [[]for i in range(V)]
hq = [(0, r)] #(distance, node)
dist[r] = 0
H = list(map(int,input().split()))
seen = [False] * V # ノードが確定済みかどうか
for i in range(E):
    u,v = map(lambda x:int(x)-1,input().split())
    if H[u]>H[v]:
        u,v = v,u
    dif = H[v]-H[u]
    G[u].append([dif,v])
    G[v].append([0,u])
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    #print(v)
    seen[v] = True
    for i in G[v]: # ノード v に隣接しているノードに対して
        if seen[i[1]] == False and dist[v] + i[0] < dist[i[1]]:
            dist[i[1]] = dist[v] + i[0]
            heappush(hq, (dist[i[1]], i[1]))
    #print(dist)
ans = [dist[i]+H[i] for i in range(V)]
print(ans[0]-min(ans))
