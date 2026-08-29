T = int(input())
from collections import deque
import sys
input = sys.stdin.readline
for case in range(T):
    N,M = map(int,input().split())
    C = list(map(int,input().split()))
    G = [[] for i in range(N)]
    for i in range(M):
        u,v = map(int,input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    dist = [-1 for i in range(N*N)]
    q = deque()
    dist[N-1]=0
    q.append(N-1)
    while q:
        vivj = q.popleft()
        vi = vivj//N
        vj = vivj%N
        for i in G[vi]:
            for j in G[vj]:
                if C[i]==C[j]:
                    continue
                if dist[i*N+j]!=-1:
                    continue
                dist[i*N+j]=dist[vi*N+vj]+1
                q.append(i*N+j)
    print(dist[(N-1)*N])