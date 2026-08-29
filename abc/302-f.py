from heapq import heappush, heappop
N,M = map(int,input().split())
V = M+N
dist = [-1] * V
G = [[]for i in range(V)]
r = 0
hq = [(0, r)] #(distance, node)
dist[r] = 0
for i in range(N):
    A = int(input())
    S = list(map(int,input().split()))
    for j in range(A):
        G[S[j]-1].append(M+i)
        G[M+i].append(S[j]-1)
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    #print(v)
    for i in G[v]: # ノード v に隣接しているノードに対して
        if dist[i]==-1:
            dist[i] = dist[v] + 1
            heappush(hq, (dist[i], i))
    #print(dist)
if dist[M-1] == -1:
    print(-1)
else:
    print(dist[M-1]//2-1)
