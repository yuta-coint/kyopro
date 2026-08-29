N = int(input())
C = [list(input()) for i in range(N)]
G=[[] for i in  range(N*N)]
#(i,j)から遷移できる状態を列挙する。
for i in range(N):
    for j in range(N):
        for k in range(N):
            if C[i][k]=="-":
                continue
            for l in range(N):
                if C[i][k]==C[l][j]:
                    G[k*N+l].append(i*N+j)
#ゴールは、対角線か、辺で繋がっているもの
from heapq import heappush, heappop
INF = 10 ** 9
V = N*N
dist = [INF] * V
hq = []
for i in range(N):
    dist[i*N+i]=0
    hq.append((0,i*N+i))
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if C[i][j]!="-":
            hq.append((1,i*N+j))
            dist[i*N+j]=1
seen = [False] * V # ノードが確定済みかどうか
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    if seen[v]:
        continue
    #print(v)
    seen[v] = True
    for i in G[v]: # ノード v に隣接しているノードに対して
        if seen[i] == False and dist[v] + 2 < dist[i]:
            dist[i] = dist[v] + 2
            heappush(hq, (dist[i], i))
    #print(dist)
ans = [[dist[i*N+j] for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if ans[i][j]==INF:
            ans[i][j]=-1
for i in range(N):
    print(*ans[i])