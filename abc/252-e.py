import sys
input = sys.stdin.readline
from heapq import heappush, heappop
V,E = map(int,input().split())
dist = [float("inf")] * V
G = [[]for i in range(V)]
r=0
hq = [(0, r,-1)] #(distance, node)
dist[r] = 0
seen = [False] * V # ノードが確定済みかどうか
for i in range(E):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    G[a].append([c,b,i+1])
    G[b].append([c,a,i+1])
ans = [0 for i in range(V)]
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    seen[v] = True
    for i in G[v]: # ノード v に隣接しているノードに対して
        if seen[i[1]] == False and dist[v] + i[0] < dist[i[1]]:
            dist[i[1]] = dist[v] + i[0]
            ans[i[1]]=i[2]
            heappush(hq, (dist[i[1]], i[1]))
    #print(dist)
ans = ans[1:]
ans.sort()
print(*ans)
