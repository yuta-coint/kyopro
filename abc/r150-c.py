import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    u,v = map(lambda x:int(x)-1,input().split())
    G[v].append(u)
    G[u].append(v)
A = list(map(lambda x:int(x)-1,input().split()))
B = list(map(lambda x:int(x)-1,input().split()))
from heapq import heappush, heappop
INF = 10 ** 9
dist = [float("inf")] * N
if A[0]==B[0]:
    hq = [(1, 0)] #(distance, node)
    dist[0]=1
else:
    hq = [(0, 0)]
    dist[0]=0
seen = [False] * N # ノードが確定済みかどうか
while hq!=[]:
    v = heappop(hq)[1] # ノードを pop する
    if seen[v]:
        continue
    #print(v)
    seen[v] = True
    for i in G[v]: # ノード v に隣接しているノードに対して
        if seen[i] == False:
            if dist[v]==K:
                temp = K
            elif A[i]==B[dist[v]]:
                temp=dist[v]+1
            else:
                temp=dist[v]
            if temp<dist[i]:
                dist[i]=temp
                heappush(hq, (dist[i], i))
    #print(dist)
if dist[N-1]==K:
    print("Yes")
else:
    print("No")
    