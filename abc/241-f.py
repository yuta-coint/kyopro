from bisect import bisect_left
from heapq import heappush, heappop
from collections import defaultdict
H,W,N = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
dif = [[0,1],[-1,0],[0,-1],[1,0]]
dx = defaultdict(list)
dy = defaultdict(list)
stones = []
for i in range(N):
    x,y = map(int,input().split())
    stones.append((x,y))
    dx[x].append(y)
    dy[y].append(x)
V = 4*N
index = {stones[i][0]*W+stones[i][1]:i for i in range(N)}
dist = [float("inf")] * (V+2)
G = [[]for i in range(V+2)]
for L in dx.keys():
    dx[L].sort()
for L in dy.keys():
    dy[L].sort()
spin = [-1,1]
for i in range(N):
    for s in range(2):
        x,y = stones[i][0],stones[i][1]+spin[s]
        if y in dy:
            if dy[y][0]<x:
                G[4*i+s*2].append(4*index[dy[y][bisect_left(dy[y],x)-1]*W+y]+3)
            if x<dy[y][-1]:
                G[4*i+s*2].append(4*index[dy[y][bisect_left(dy[y],x)]*W+y]+1)
        x,y = stones[i][0]+spin[s],stones[i][1]
        if x in dx:
            if dx[x][0]<y:
                G[4*i+1+s*2].append(4*index[W*x+dx[x][bisect_left(dx[x],y)-1]]+2)
            if y<dx[x][-1]:
                G[4*i+1+2*s].append(4*index[W*x+dx[x][bisect_left(dx[x],y)]])
x,y = sx,sy
if y in dy:
    if dy[y][0]<x:
        G[V].append(4*index[dy[y][bisect_left(dy[y],x)-1]*W+y]+3)
    if x<dy[y][-1]:
        G[V].append(4*index[dy[y][bisect_left(dy[y],x)]*W+y]+1)
if x in dx:
    if dx[x][0]<y:
        G[V].append(4*index[W*x+dx[x][bisect_left(dx[x],y)-1]]+2)
    if y<dx[x][-1]:
        G[V].append(4*index[W*x+dx[x][bisect_left(dx[x],y)]])
gg = [(gx,gy+1),(gx+1,gy),(gx,gy-1),(gx-1,gy)]
goal = []
for i in range(N):
    for j in range(4):
        if stones[i]==gg[j]:
            goal.append(4*i+j)
hq = [(0, V)] #(distance, node)
dist[V] = 0
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    #print(v)
    for i in G[v]: # ノード v に隣接しているノードに対して
        if dist[i]==float('inf'):
            dist[i] = dist[v] + 1
            heappush(hq, (dist[i], i))
#print(G)
#print(dist)
#print(goal)
#目的地はどこ？
ans = float('inf')
for i in goal:
    ans = min(ans,dist[i])
if ans ==float('inf'):
    print(-1)
else:
    print(ans)