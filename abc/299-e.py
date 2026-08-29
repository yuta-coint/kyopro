from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = 10 ** 9
V,E = map(int,input().split())
G = [[]for i in range(V)]
for i in range(E):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
def dj(r):
    dist = [INF] * V
    hq = [(0, r)] #(distance, node)
    dist[r] = 0
    while hq!=[]:
        v = heappop(hq)[1] # ノードを pop する
        #print(v)
        for i in G[v]: # ノード v に隣接しているノードに対して
            if dist[i]==INF:
                dist[i] = dist[v] + 1
                heappush(hq, (dist[i], i))
    #print(dist)
    return dist
dt = [dj(i) for i in range(V)]
white = [1 for i in range(V)]
K = int(input())
conditions = [tuple(map(int,input().split())) for i in range(K)]
#黒く塗れない辺を確定させる
for p,d in conditions:
    for i in range(V):
        if dt[p-1][i]<d:
            white[i]=0
#全部塗ればいいじゃん
for p,d in conditions:
    for i in range(V):
        if dt[p-1][i]*white[i]==d:
            break
    else:
        print("No")
        exit()
print("Yes")
print(*white,sep="")