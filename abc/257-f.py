import sys
input = sys.stdin.readline
from heapq import heappush, heappop
V,E = map(int,input().split())
V+=1
r = 1
dist = [-1] * V
G = [[]for i in range(V)]
for i in range(E):
    a,b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)
hq = [(0, r)] #(distance, node)
dist[r] = 0
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    #print(v)
    for i in G[v]: # ノード v に隣接しているノードに対して
        if dist[i]==-1:
            dist[i] = dist[v] + 1
            heappush(hq, (dist[i], i))
    #print(dist)
r = V-1
dist2 = [-1] * V
hq = [(0, r)] #(distance, node)
dist2[r] = 0
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    #print(v)
    for i in G[v]: # ノード v に隣接しているノードに対して
        if dist2[i]==-1:
            dist2[i] = dist2[v] + 1
            heappush(hq, (dist2[i], i))
    #print(dist)
p = []
for i in range(1,V):
    ans = dist2[1]
    if ans==-1:
        ans = float('inf')
    if dist2[i]!=-1 and dist[0]!=-1:
        ans = min(ans,dist2[i]+dist[0])
    if dist2[0]!=-1 and dist[i]!=-1:
        ans = min(ans,dist[i]+dist2[0])
    if ans==float('inf'):
        p.append((-1))
    else:
        p.append((ans))
print(*p)