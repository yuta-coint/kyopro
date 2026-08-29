from heapq import heappush, heappop
INF = 10 ** 9
V,E,r = map(int,input().split())
dist = [INF] * V
G = [[]for i in range(V)]
hq = [] #(distance, node)
seen = [False] * V # ノードが確定済みかどうか
for i in range(E):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
for i in range(r):
    p,h = map(int,input().split())
    heappush(hq,(-h,p-1))
    dist[p-1]=-h
#print(G)
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    if seen[v]:
        continue
    #print(v)
    seen[v] = True
    for i in G[v]: # ノード v に隣接しているノードに対して
        if seen[i] == False and dist[v] + 1 < dist[i]:
            dist[i] = dist[v] + 1
            heappush(hq, (dist[i], i))
#print(dist)
ans = []
for i in range(V):
    if dist[i]<=0:
        ans.append(i+1)
print(len(ans))
print(*ans)
