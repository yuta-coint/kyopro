#「木の直径の大きい方」か「結んだ二点から一番遠いとこまでの距離+1」のうち大きい方
import sys
from collections import deque
sys.setrecursionlimit(300000)
import copy
for k in range(2):
    N =  int(input())
    G=[[] for i in range(N+1)]
    for i in range(N-1):
        u,v = map(lambda x:int(x)-1,input().split())
        G[u].append(v)
        G[v].append(u)
    for i in range(N+1):G[i].sort()
    def bfsdj(r):
        hq = deque()
        hq.append((0, r)) #(distance, node)
        dist = [-1] * N
        dist[r] = 0
        while hq!=[]:
            v = hq.popleft()[1] # ノードを pop する
            #print(v)
            for i in G[v]: # ノード v に隣接しているノードに対して
                if dist[i]==-1:
                    dist[i] = dist[v] + 1
                    hq.append((dist[i], i))
            #print(dist)
        return dist
    dist_temp = bfsdj(0)
    #print(dist_temp)
    M = max(dist_temp)
    S = dist_temp.index(M)
    dist_s = bfsdj(S)
    M = max(dist_s)
    T = dist_s.index(M)
    dist_t = bfsdj(T)
    if k==0:
        U0 = [max(dist_s[i],dist_t[i]) for i in range(N)]
        U0.sort()
        M0 = M
    else:
        U1 = [max(dist_s[i],dist_t[i]) for i in range(N)]
        U1.sort()
        M1 = M
from bisect import bisect_left
#print(U0,U1)
N0 = len(U0)
N1 = len(U1)
ans = N0*N1
D = max(M1,M0)-1
for i in U0:
    temp = bisect_left(U1,D-i)
    ans += D*temp+i*(N1-temp)
for i in U1:
    temp = bisect_left(U0,D-i)
    ans += i*(N0-temp)
print(ans)
