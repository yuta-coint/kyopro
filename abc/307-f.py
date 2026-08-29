import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G = [{} for i in range(N)]
for i in range(M):
    u,v,w = map(int,input().split())
    G[u-1][v-1]=w
    G[v-1][u-1]=w
from heapq import heapify,heappop,heappush
next = []
heapify(next)
K = int(input())
A = list(map(int,input().split()))
D = int(input())
X = list(map(int,input().split()))
ans = [-1 for i in range(N)]
for a in A:
    ans[a-1] = 0
    for k in G[a-1]:
        heappush(next,(G[a-1][k],k))
for i in range(D):
    waiting = []
    while next:
        d,v = heappop(next)
        if d>X[i]:
            heappush(next,(d,v))
            #print(d,v)
            break
        if ans[v]>=0:
            continue
        ans[v]=i+1
        for k in G[v]:
            waiting.append((G[v][k],k))
            #print(G[v][k],k)
            heappush(next,(d+G[v][k],k))
            #print(G[v][k]+d,k)
    for wait in waiting:
        heappush(next,wait)
        #print(wait)
for i in range(N):
    print(ans[i])