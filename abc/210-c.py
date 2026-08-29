from heapq import heappush, heappop
import sys
input = sys.stdin.readline
mod = 10**9+7
V = int(input())
r,B = map(int,input().split())
E = int(input())
dist = [-3] * V
G = [[]for i in range(V)]
pat = [0]*(V)
pat[r-1] = 1
hq = [(0, r-1)] #(distance, node)
dist[r-1] = 0
for i in range(E):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
while hq!=[]:
    v = heappop(hq)[1]
     # ノードを pop する
    #print(v)
    for i in G[v]: # ノード v に隣接しているノードに対して
        if dist[i]==-3:
            dist[i] = dist[v] + 1
            heappush(hq, (dist[i], i))
            pat[i] += pat[v]
        elif dist[i] == dist[v] + 1:
            pat[i]+=pat[v]
        pat[i]%=mod

    #print(dist)
print(pat[B-1])
