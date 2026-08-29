import sys
input = sys.stdin.readline
N,M = map(int,input().split())
W = list(map(int,input().split()))
G = [set() for i in range(N)]
INF = 10**18
dist =[INF for j in range(N*N)]
seen =[False for j in range(N*N)]
for i in range(N):
    dist[i] = 0
for i in range(M):
    u,v = map(int,input().split())
    G[u-1].add(v-1)
    G[v-1].add(u-1)
for d in reversed(range(1,N)):
    for v in range(N):
        #print(v)
        seen[v * N  + d] = True
        for i in G[v]: # ノード v に隣接しているノードに対して
            if seen[i*N + d-1] == False and dist[v * N +d] + W[v] * d < dist[i * N + d-1]:
                dist[i * N + d-1] = dist[v * N + d] + W[v] * d
for i in range(N):
    ans = INF
    for j in range(i*N,i*N + N):
        if dist[j] < ans:
            ans = dist[j]
    print(ans)